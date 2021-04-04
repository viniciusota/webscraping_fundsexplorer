import pandas as pd 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import sys 
sys.path.append( '../' )
import requests
import os



def get_url_list(list_fii):
    list_url = []
    for name in list_fii:
    	list_url.append("https://query1.finance.yahoo.com/v7/finance/download/{}.SA?period1=1562803200&period2=1617408000&interval=1d&events=history&includeAdjustedClose=true".format(name))
    return list_url ; 



def save_files(list_url,list_fii):
    for url,name_fii in zip( list_url , list_fii ):
        download_obj = requests.get( url )
        if download_obj.status_code == 200: 
            print( name_fii )
            with open('historical_data/data/{}.csv'.format(name_fii), "wb") as file:
                file.write(download_obj.content)

if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath('__file__') ) 
    file_path = os.path.join( path , 'DataSet_Fii.csv' )
    
    data = pd.read_csv( file_path , usecols=['codigodofundo'])
    print("read data")
    list_url = get_url_list( data['codigodofundo'] )
    print("Created Url")
    print(os.listdir())
    save_files( list_url , data['codigodofundo'] )
