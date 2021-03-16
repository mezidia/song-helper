"""Search song on YouTube"""
import requests
from bs4 import BeautifulSoup

URL = 'https://www.youtube.com/results?search_query=python'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36',
    'accept': '*/*'}
