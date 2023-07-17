from fastapi import FastAPI
from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your React app's origin
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

client = MongoClient("mongodb+srv://gauravpadam2:Growisto12ee1122@cluster0.7qcntfh.mongodb.net/")
db = client["Articles"]
collection = db["Articlecollection"]

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
        img_src = picture.find('img', src=True)['src']
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
scheduler.add_job(scrape_and_store, 'interval', hours=24)
scheduler.start()

# Ensure that the scheduler is properly shut down when the application exits
@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown(wait=False)
