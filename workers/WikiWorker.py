import requests 
from bs4 import BeautifulSoup

class WikiWorker():
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    def get_sp_500_companies(self):
        response = requests.get(self.url)
        
