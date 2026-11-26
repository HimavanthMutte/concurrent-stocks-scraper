import threading
import requests 
from lxml import html 
import time 
import random 

class YahooFinancePriceWorker(threading.Thread):
    base_url = "https://finance.yahoo.com/quote/"

    def __init__(self,symbol):
        super().__init__()
        self.symbol = symbol 
        self.url = f"{self.base_url}{self.symbol}"

    def run(self):
        time.sleep(30 * random.random())
        r = requests.get(self.url)
        if r.status_code!=200:
            return
        page_contents = html.fromstring(r.text)
        price = float(page_contents.xpath('/html/body/div[2]/div[4]/main/section/section/section/section/section[1]/div[2]/div[1]/section/div/section[1]/div[1]/span[1]')[0].text)
        print(price)