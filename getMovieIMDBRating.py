# This program takes movie name as imput and returns the IMDB rating for the movie

import requests
from lxml import html
import datetime
import subprocess as s

def getSiteContent(url):
    siteContent=requests.get(url)
    htmlTree=html.fromstring(siteContent.content)
    #print(htmlTree.xpath('//*[@id="search"]/div/h1/text()'))
    return htmlTree

#-----------to get the IMDB title URL----------------
def getIMDBUrl(mname):
    searchText=mname #+'+2018'
    imdbUrl='https://www.imdb.com/find?s=all&q='+searchText
    #print(imdbUrl)
    htmlTreeIMDB=getSiteContent(imdbUrl)
    imdbMTitle=htmlTreeIMDB.xpath('//td[@class="result_text"]/a/@href')
    imdbMTitle='https://www.imdb.com/'+imdbMTitle[0]
    #print(imdbMTitle)
    return imdbMTitle
#----end of-------to get the IMDB title URL----------------    

#-----------to get the rating from IMDB-----------------
def getMovieIMDBRating(moviename):
    url=getIMDBUrl(moviename)
    htmlTreeIMDB=getSiteContent(url)
    try:
        rating=htmlTreeIMDB.xpath('//div[@class="ratingValue"]/strong/span/text()')
    except:
        print('No rating found! ')    
    #stars=htmlTreeIMDB.xpath('//div[@class="rec-actor rec-ellipsis"]/span/text()')
    #print(stars)
    if len(rating)>=1:
        return float(rating[0])
    
#-----end of------to get the rating from IMDB-----------------


if __name__=='__main__':
    movieName=input('Please enter movie name? ')

    if movieName!="":
        rating=getMovieIMDBRating(movieName)
        print(rating)
        #if rating>0:
        #    msg=movieName+'-'+str(rating) + ' (IMDB Rating) '
        #    if float(rating)>=6:
        #        s.call(["notify-send","-i","face-laugh",msg])            #this will send desktop notification, to print the output in
        #    else:
        #        s.call(["notify-send","-i","face-monkey",msg])
        #else:
        #    print("No rating found ! ")

        #url=getIMDBUrl(movieName)
        #print(url)
    else:
        print('Please enter movie name!')
        movieName=input()