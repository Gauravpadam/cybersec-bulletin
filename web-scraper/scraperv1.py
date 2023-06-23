import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    session = requests.Session()
    response = session.get(url)
    html_content = response.text
    links = []
    soups = []
    articledata = {'Title': [], 'Body': [], 'img': []}

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
    for soup in soups:
        title = soup.select_one('title').text
        summary = soup.select_one('.summary').get_text()
        picture = soup.select_one('picture')
        img_src = picture.find('img' , src=True)['src']
        articledata['Title'].append(title)
        articledata['Body'].append(summary)
        articledata['img'].append(img_src)

    print(articledata)


# Example usage
url = "https://www.darkreading.com/vulnerabilities-threats"  # Replace with the actual URL of the site
scrape_data(url)
