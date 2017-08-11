# created on 11/08/2017
#future enhancement : send response in json format with train details

from bs4 import BeautifulSoup as soup
import requests
import json

base_url='https://www.trainspnrstatus.com/trains'


def getTrainDetails(s_html):
    if s_html=='404 Page':
       print('Train not found')
    else:
        train_details=s_html.findAll('li',{'class':'list-group-item list-group-item-info'})
        for detail in train_details:
            print(detail.text)

def getHtml(url):
    try:
        html_response=requests.get(url)
        if html_response.status_code==200:
            return soup(html_response.content,'html.parser')
        elif html_response.status_code==404:
            return soup(html_response.content,'html.parser')
        else:
            return "Train not found !"
    except Exception:
            pass

if __name__=='__main__':
    from_station=raw_input('Please enter From station name:')
    to_station=raw_input('Please enter To station name:')

    if from_station!="" and to_station!="":
        url=base_url+'/'+from_station+'-'+to_station
        try:
           soup_html=getHtml(url)
        except Exception:
            pass
        
        if soup_html.is_empty_element==False:
            getTrainDetails(soup_html)
        else:
            print(soup_html)
    else:
        print("Invalid Station Name!")


    
