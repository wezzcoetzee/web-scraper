from dotenv import load_dotenv
import os

load_dotenv()

# e.g URL https://www.example.com
TEXT_URL_TO_SCRAPE = os.getenv('TEXT_URL_TO_SCRAPE')
YOUTUBE_URL_TO_SCRAPE = os.getenv('YOUTUBE_URL_TO_SCRAPE')
BASE_URL = os.getenv('BASE_URL')
HEADER_SLUGS = os.getenv('HEADER_SLUGS')
CONTENT_SLUGS = os.getenv('CONTENT_SLUGS')