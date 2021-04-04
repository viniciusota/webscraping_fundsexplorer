from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import unicodedata




def get_html( URL ):
    """ Parsing the html page: 
        This function recieve an url to be parsed
    """
    url = URL
    req= Request(url)
    req= Request(url, headers={'User-Agent':'Mozzila/5.0'})
    response=urlopen(req)
    html = response.read()
    soup=BeautifulSoup(html,'html.parser')
    return soup ; 


def get_fii_table( soup ): 
    rows = []
    for tr in soup.select('tr'):
        rows.append([td.get_text(strip=True) for td in tr.select('th, td')])
    return rows

def create_dataframe( rows ): 
    Data = pd.DataFrame( rows[ 1:len(rows) ] , columns = rows[0] )
    return Data

def columns_name(word):
    nfkd = unicodedata.normalize('NFKD', word)
    word_without_special_char = u"".join([c for c in nfkd if not unicodedata.combining(c)])    
    word_without_special_char = word_without_special_char.lower()
    word_without_special_char = word_without_special_char.replace( '(' , '_'  )
    word_without_special_char = word_without_special_char.replace( ')' , '_')
    word_without_special_char = word_without_special_char.replace(' ' , '')
    return word_without_special_char ; 


if __name__=='__main__':
    soup_obj = get_html(  'https://www.fundsexplorer.com.br/ranking' ) 
    list_data = get_fii_table( soup = soup_obj ) 
    DataSet = create_dataframe( rows = list_data )
    names = [ columns_name( col ) for col in DataSet.columns ]
    DataSet.columns = names 
    DataSet.to_csv( 'DataSet_Fii.csv' , index = False  )



    #Here we should save the file into s3 bucket , using the function: upload_file_into_s3_bucket( data , "my_bucket_path" ) 
    #But here i'll save it locally:
    # DataSet_Fii_Name.to_csv( 'fii_name.csv' , index = False )







