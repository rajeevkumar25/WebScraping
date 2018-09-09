#----Authored by Rajeev Kumar on 09/10 ----------------------
#--------------The Program scapes money control site and gets the top gainer stocks and best mutual fund information in most raw format

import requests
from lxml import html
import time
import sys

def getSiteContent(url):
    siteContent=requests.get(url)
    htmlTree=html.fromstring(siteContent.content)
    #print(htmlTree.xpath('//*[@id="search"]/div/h1/text()'))
    return htmlTree


def getStocksData():
    mcStocksUrl='https://www.moneycontrol.com/'
    
    mcHtmlTreeStocks=getSiteContent(mcStocksUrl)
    tGainCmp=mcHtmlTreeStocks.xpath('//div[@id="tgNifty"]/table/tbody/tr/td/a/text()')
    tGainPrices=mcHtmlTreeStocks.xpath('//div[@id="tgNifty"]/table/tbody/tr/td[2]/b/text()')
    tGainChange=mcHtmlTreeStocks.xpath('//div[@id="tgNifty"]/table/tbody/tr/td[3]/text()')
    tGainPerChng=mcHtmlTreeStocks.xpath('//div[@id="tgNifty"]/table/tbody/tr/td[4]/text()')

    tGainDetails=zip(tGainCmp,tGainPrices,tGainChange,tGainPerChng)
    print("Compnay","Price","Change","%Change")
    for item in tGainDetails:
        print(item)

def getMutualFundData():
    mcMutualFundUrl='https://www.moneycontrol.com/mutualfundindia/'

    mcHtmlTreeMF=getSiteContent(mcMutualFundUrl)
    i=1
    print("Fund Name","6 Months (%)","1 Year (%)","3 Year (%)")
    for i in range(1,5):
        mfName=mcHtmlTreeMF.xpath(('//div[@id="mf_all"]/div/div/table[{}]/tbody[2]/tr/td/a/text()').format(i))
        mfSixMonRetrn=mcHtmlTreeMF.xpath(('//div[@id="mf_all"]/div/div/table[{}]/tbody[2]/tr/td[3]/span/text()').format(i))
        mfYearRetrn=mcHtmlTreeMF.xpath(('//div[@id="mf_all"]/div/div/table[{}]/tbody[2]/tr/td[4]/span/text()').format(i))
        mfThreeYrRetrn=mcHtmlTreeMF.xpath(('//div[@id="mf_all"]/div/div/table[{}]/tbody[2]/tr/td[5]/span/text()').format(i))
        
        mfDetails=zip(mfName,mfSixMonRetrn,mfYearRetrn,mfThreeYrRetrn)

        for mf in mfDetails:
            print(mf)
        print("=======================")    
        time.sleep(2)


if __name__=='__main__':
    fundType=raw_input('What info do you need? Stocks or  Mutual Fund ? -')
    if fundType!="":
        fundType=fundType.lower()       
        if fundType.strip()=='stocks':
            getStocksData()
        elif fundType.strip()=='mutual fund' or fundType=='mf':
            getMutualFundData()
    else:
        print('Invalid entry !')
        sys.exit(1)