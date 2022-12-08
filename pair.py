from statsmodels.tsa.stattools import coint


class Pair():
    def __init__(self, stock1, stock2):
        self.stock1 = stock1
        self.ticker1 = stock1.ticker
        self.stock2 = stock2
        self.ticker2 = stock2.ticker

    def calc_engle_granger(self):
        self.coint = coint(self.stock1.close,self.stock2.close)
