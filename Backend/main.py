from fastapi import FastAPI
from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware
import os  # Import the 'os' module

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your React app's origin
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Define collection as a global variable
client = MongoClient("mongodb://mongo:27017/")
db = client["Articles"]
collection = db["Articlecollection"]

# Function to initialize the database and collection
def initialize_database():
    # Check if the collection exists, and create it if not
    if collection.name not in db.list_collection_names():
        db.create_collection(collection.name)

# Call the initialization function when the application starts
initialize_database()

def scrape_and_store():
    url = "https://www.darkreading.com/vulnerabilities-threats"

    session = requests.Session()
    response = session.get(url)
    html_content = response.text
    links = []
    soups = []
    articledata = []

    # Parse the HTML content using Beautiful Soup
    mainsoup = BeautifulSoup(html_content, "lxml")
    articles = mainsoup.find_all("div", class_="topic-content-article")

    # First pass fetching links and creating soups
    for article in articles:
        link = article.find("a", href=True)['href']
        res = session.get(link)
        soup = BeautifulSoup(res.text, "lxml")
        soups.append(soup)
        links.append(link)

    # Second pass extracting data from soups
    id = 0
    for soup in soups:
        id += 1
        title = soup.select_one('title').text
        summary = soup.select_one('.summary').get_text()
        picture = soup.select_one('picture')
        if picture:
            img_src = picture.find('img', src=True)['src']
        else:
            img_src="https://eu-images.contentstack.com/v3/assets/blt66983808af36a8ef/blt0081f3369307d97f/61e87ceed912285939eb7b20/DDoS_Aleksey_Funtap_Alamy.jpg?quality=80&format=webply&width=690"
            pass # Frontend will handle no image case
        articledata.append({'Articleid': id, 'Title': title, 'Summary': summary, 'Picture': img_src , 'Link': links[id-1]})

    # Store the data in MongoDB
    collection.delete_many({})  # Clear existing data
    collection.insert_one({"data": articledata})

@app.get("/data/1")
def get_data1():
    data = collection.find_one({}, {"_id": 0})
    return data["data"][:6]

@app.get("/data/2")
def get_data2():
    data = collection.find_one({}, {"_id": 0})
    return data["data"][6:12]

@app.get("/data/3")
def get_data3():
    data = collection.find_one({}, {"_id": 0})
    return data["data"][12:15]

scheduler = BackgroundScheduler()

# Initial scrape on application start
scrape_and_store()

# Schedule subsequent scrapes every 24 hours
scheduler.add_job(scrape_and_store, 'interval', hours=1)
scheduler.start()

# Ensure that the scheduler is properly shut down when the application exits
@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown(wait=False)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
