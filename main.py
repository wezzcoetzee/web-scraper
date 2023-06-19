import requests
from bs4 import BeautifulSoup


def domain_scraper(domain):
    url = f'http://{domain}'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Define the HTML tags to extract
    tags = ['p', 'a', 'li', 'h1', 'h2', 'h3']

    text = []
    for tag in tags:
        elements = soup.find_all(tag)
        for element in elements:
            text.append(element.get_text())

    return ' '.join(text)


# Replace 'yourdomain.com' with your actual domain
text = domain_scraper('yourdomain.com')
print(text)