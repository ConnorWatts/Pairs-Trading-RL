
import argparse
import data.utils as data
import utils


def main(config):

    # change each config to config[''] (TO DO)

    # prepare data
    data.prepare_data(config)

    # create stocks
    stocks = utils.get_stocks(config)

    # create pairs
    pairs = utils.get_pairs(config,stocks)

    # cointegration check (TO DO)
    # pairs_train = utils.filter_pairs(config[''],pairs)
    pairs_train = pairs


    pass




def get_args():

    parser = argparse.ArgumentParser(description='DQN Pairs Trading')

    args = parser.parse_args()

    # Wrapping training configuration into a dictionary
    training_config = dict()
    for arg in vars(args):
        training_config[arg] = getattr(args, arg)

    return training_config




if __name__ == '__main__':
    main(get_args())



"""from utils import download_stock_list, get_list_csv, get_distinct_pairs, \
     download_stock_data,remove_futures

import pandas as pd
from stock import Stock
from pair import Pair

def main(params):

    # if not all ready download list of stocks from wiki page for SP500
    if params["download_stock_list"]: download_stock_list(params)

    stocks = []
    
    #put in utils function
    #tickers_ = get_list_csv('stock_list.csv')
    tickers_ = ["AAPL","AAP","ABBV","ABMD","ABT","ACN","ADBE"]

    if params["download_stock_data"]: download_stock_data(tickers_)

    #create stock objects and get data 
    for s in list(tickers_):
        stock = Stock(s)
        stock.get_history_csv()
        stocks.append(stock)

    pairs = get_distinct_pairs(stocks)

    pairs_ = [Pair(pair[0],pair[1]) for pair in pairs]

    for pair in pairs_:
        pair.calc_engle_granger()
        print(pair.coint)

    pass


"""