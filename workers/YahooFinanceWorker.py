import threading
import requests 
from lxml import html 
import time 
import random 

class YahooFinancePriceWorker(threading.Thread):
    base_url = "https://finance.yahoo.com/quote/"

    def __init__(self,symbol):
        super().__init__(daemon=False)
        self.symbol = symbol 
        self.url = f"{self.base_url}{self.symbol}"

    def run(self):
        print(f"[{self.symbol}] Thread started")

        delay = 30 * random.random()
        print(f"[{self.symbol}] Sleeping for {delay:.2f} seconds")

        time.sleep(delay)

        print(f"[{self.symbol}] Fetching price")

        r = requests.get(self.url)

        print(f"[{self.symbol}] Status code: {r.status_code}")

        if r.status_code != 200:
            print(f"[{self.symbol}] Request failed")
            return

        page_contents = html.fromstring(r.text)

        price = float(
            page_contents.xpath(
                '/html/body/div[2]/div[4]/main/section/section/section/section/section[1]/div[2]/div[1]/section/div/section[1]/div[1]/span[1]'
            )[0].text
        )

        print(f"[{self.symbol}] Price: {price}")