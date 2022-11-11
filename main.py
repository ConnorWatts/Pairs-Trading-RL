from utils import download_stock_list, get_list_csv, get_distinct_pairs, download_stock_data,remove_futures


import pandas as pd
from stock import Stock

def main(params):

    # if not all ready download list of stocks from wiki page for SP500
    if params["download_stock_list"]: download_stock_list(params)

    stocks = []
    
    #put in utils function
    #tickers_ = get_list_csv('stock_list.csv')
    #print(len(tickers_))
    #tickers_ = remove_futures(tickers_,"=F")
    #print(len(tickers_))
    tickers_ = ["AAPL","AAP","ABBV","ABMD","ABT","ACN","ADBE"]

    if params["download_stock_data"]: download_stock_data(tickers_)

    #create stock objects and get data 
    for s in list(tickers_):
        stock = Stock(s)
        stock.get_history_csv()
        stocks.append(stock)

    pairs = get_distinct_pairs(stocks)
    #print(pairs)

    


    #find and create pair objects

    #get and save data as selenium
    #create stock classes (maybe getting the data is a method in class)

    pass


if __name__ == '__main__':
    params = {"download_stock_list":False,"download_stock_data":True}
    main(params)