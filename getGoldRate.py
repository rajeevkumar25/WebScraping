import requests
from lxml import html

url='https://www.policybazaar.com/'

def getGoldRate(cityName):
    actual_site=url+'gold-rate-'+cityName+'/'
    #print(actual_site)
    site_content=requests.get(actual_site)
    html_tree=html.fromstring(site_content.content)
    #rate=html_tree.xpath('//*[@id="content"]/div[14]/div/div/div[1]/div/div/div[1]/div[1]/text()')
    rate=html_tree.xpath('//div[@class="dailyGoldrate"]/text()')
    if len(rate)==0:
        print('Gold rate not found for '+ cityName+ '!')
    else:
        print(rate)

if __name__=='__main__':
    city=input('Which City gold rate you want to check? ')
    if city!="":
        getGoldRate(city)
    else:
        city=input('Please enter city name! ')
        getGoldRate(city)
    
