import requests
from bs4 import BeautifulSoup

def scrape_data(link):
    response = requests.get(link)
    html_content = response.text

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, "lxml")

    print(html_content)

# Example usage
link = "https://www.bleepingcomputer.com/news/security/"  # Replace with the actual URL of the site
scrape_data(link)
