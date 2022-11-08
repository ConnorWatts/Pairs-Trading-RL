import pandas as pd 
import requests 
from bs4 import BeautifulSoup 


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

