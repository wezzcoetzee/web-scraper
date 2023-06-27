import json
import re
import requests
from bs4 import BeautifulSoup
from settings import TEXT_BASE_URL_TO_SCRAPE, TEXT_DATA_URL_TO_SCRAPE, CONTENT_TEXT_DATA_URL_TO_SCRAPE
from models import UrlModel


urls_to_scrape = [UrlModel(TEXT_DATA_URL_TO_SCRAPE, "Headers.txt"),
                  UrlModel(CONTENT_TEXT_DATA_URL_TO_SCRAPE, "Content.txt")]


def domain_scraper(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    tags = ['p', 'a', 'li', 'h1', 'h2', 'h3']

    text = []
    for tag in tags:
        elements = soup.find_all(tag)
        for element in elements:
            text.append(element.get_text())

    return ' '.join(text)


def get_subpages(url, file_name):
    response = requests.get(url)

    json_pattern = r'\[\{(.*?)\}\]'
    match = re.search(json_pattern, response.text)

    if match:
        extracted_string = match.group(0)
        sub_pages = json.loads(extracted_string)

        for sub_page in sub_pages:
            try:
                link_suffix = sub_page['url']
                link = f"{TEXT_BASE_URL_TO_SCRAPE}{link_suffix}"
                print(link)
                write_output(link, file_name)
            except KeyError:
                print("Not a valid subpage, skipping")
    else:
        print("No match found.")


def write_output(link, file_name):
    content = domain_scraper(link);
    print(content)
    file_path = f"output/{file_name}"  # Replace with the actual file path
    file = open(file_path, 'w')
    file.write('\n' * 5 + content)
    file.close()


for url_to_scrape in urls_to_scrape:
    get_subpages(url_to_scrape.url, url_to_scrape.filename)
