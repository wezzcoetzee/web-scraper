from dotenv import load_dotenv
import os

load_dotenv()

# e.g URL https://www.example.com
TEXT_URL_TO_SCRAPE = os.getenv('TEXT_URL_TO_SCRAPE')
YOUTUBE_URL_TO_SCRAPE = os.getenv('YOUTUBE_URL_TO_SCRAPE')
TEXT_BASE_URL_TO_SCRAPE = os.getenv('TEXT_BASE_URL_TO_SCRAPE')
TEXT_DATA_URL_TO_SCRAPE = os.getenv('TEXT_DATA_URL_TO_SCRAPE')