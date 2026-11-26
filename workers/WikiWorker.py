import requests 
from bs4 import BeautifulSoup

class WikiWorker():
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    def _extract_company_symbols(self,page_html):
            soup = BeautifulSoup(page_html,"lxml")
            table = soup.find(id="constituents")
            if table is None:
                 return
            table_entries = table.find_all("tr")
            for table_row in table_entries[1:]:
                  symbol_cell = table_row.find('td')
                  if symbol_cell is None:
                      continue
                  symbol = symbol_cell.text.strip("\n")
                  yield symbol

    def get_sp_500_companies(self):
        headers = {
        "User-Agent": "StockPriceScraper/1.0 (educational project)"
        }
        response = requests.get(self.url,headers=headers)
        if (response.status_code!=200):
            print("Couldn't get entries")
            return []
        yield from self._extract_company_symbols(response.text)


