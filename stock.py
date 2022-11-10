import pandas as pd

class Stock():
    def __init__(self, ticker):
        self.ticker = ticker

    def get_history_csv(self):
        self.close = pd.read_csv(".\data\{0}.csv".format(self.ticker), \
            parse_dates=True, index_col='Date',usecols=["Date","Close"])
