import time

from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorker import YahooFinancePriceWorker

def main():
    scrapper_start_time = time.time()
    wikiWorker = WikiWorker()
    current_workers = []
    for symbol in wikiWorker.get_sp_500_companies():
        yahooFinancePriceWorker = YahooFinancePriceWorker(symbol=symbol)
        current_workers.append(yahooFinancePriceWorker)
        yahooFinancePriceWorker.start()
        time.sleep(2)

    for i in range(len(current_workers)):
        current_workers[i].join()

    print("Extracting Time Took:", round(time.time() - scrapper_start_time, 1))

if __name__=="__main__":
    main()