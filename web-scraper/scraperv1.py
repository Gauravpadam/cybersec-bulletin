def main():
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
main()