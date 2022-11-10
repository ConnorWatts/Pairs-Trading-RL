import pandas as pd 
import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from os.path import exists


def download_stock_list(params):

    wikiurl: str = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    table_class="wikitable sortable jquery-tablesorter"
    response=requests.get(wikiurl)
    soup = BeautifulSoup(response.text, 'html.parser')
    indiatable=soup.find('table',{'class':"wikitable"})
    df=pd.read_html(str(indiatable))
    df=pd.DataFrame(df[0])
    df['Symbol'].to_csv('stock_list.csv') 
    pass

def download_stock_data(tickers):


    PATH = "./chromedriver/chromedriver.exe"
    chrome_opt = webdriver.ChromeOptions()
    prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": r"C:\Users\cwatts\RL Pairs\Pairs-Trading-RL\data\\", 
                 "directory_upgrade": True}
    chrome_opt.add_experimental_option('prefs', prefs)
    wd = webdriver.Chrome(executable_path=PATH, options=chrome_opt)

    def save_stock_data(wd, ticker):
        mainSite = wd.get("https://finance.yahoo.com/")
        wd.find_element(By.XPATH,"//*[@id='consent-page']/div/div/div/form/div[2]/div[2]/button").click()
        searchBox = wd.find_element(By.ID,"yfin-usr-qry")
        searchBox.send_keys("{0}".format(ticker))
        stockPg = searchBox.send_keys(Keys.RETURN)
        time.sleep(3)
        histData = wd.find_element(By.XPATH,"//*[@id='quote-nav']/ul/li[5]/a").click()
        time.sleep(2)
        timeSpan = wd.find_element(By.XPATH,"//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[1]/div/div/div[1]/span").click()
        time.sleep(2)
        dates = wd.find_element(By.XPATH,"//*[@id='dropdown-menu']/div/div[1]/input").click()
        time.sleep(2)
        dates = wd.find_element(By.XPATH,"//*[@id='dropdown-menu']/div/ul[2]/li[3]/button/span").click()
        time.sleep(2)
        dates = wd.find_element(By.XPATH,"//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[2]/span[2]/a/span").click()
        time.sleep(2)
        pass

    ticks = ["AAPL"]
    
    for tick in ticks:
        if not exists("./data/{0}.csv".format(tick)): 
            save_stock_data(wd,tick)

    pass
 
def get_list_csv(dir):

    test =pd.read_csv(dir) 
    tickers_ = test["Symbol"]
    return tickers_

def get_distinct_pairs(list_):
    output = [(a, b) for idx, a in enumerate(list_) for b in list_[idx + 1:]]
    return output


