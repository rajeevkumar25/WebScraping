import requests
from lxml import html

baseUrl='http://www.cricwaves.com/cricket/ratings'

def getUrls(ratingOf):
    if ratingOf.lower()=='team':
        teamUrl=baseUrl+'/teamratings.html'
        getTeamICCRankings(teamUrl)
    elif ratingOf.lower()=='player':
        playerUrl=baseUrl+'/playerratings.html'
        getPlayerICCRankings(playerUrl)

    
    #getICCRankings(newUrl)

def getTeamICCRankings(ratingUrl):
    if ratingUrl!="":
        siteContent=requests.get(ratingUrl)
        htmlTree=html.fromstring(siteContent.content)

        #ratings=htmlTree.xpath('//div[@class="Cf_name"]/a/div/text()')
        ratings=htmlTree.xpath('//div[@class="Cf_name"]/a/div/text()')
        #print(len(ratings))
        cntryCount=len(ratings)
        for rating in range(cntryCount):
            if rating==0:
                print("=================ODI Rankings===============")
            elif rating==10:
                print("==================Test Rankings================")
            elif rating==20:
                print("====================T20 Rankings================")    
            print(ratings[rating])
            
    else:
        print('No valid entry!')

#=============Players Ranking method============
def getPlayerICCRankings(ratingUrl):
    if ratingUrl!="":
        siteContent=requests.get(ratingUrl)
        htmlTree=html.fromstring(siteContent.content)

        #ratings=htmlTree.xpath('//div[@class="Cf_name"]/a/div/text()')
        ratings=htmlTree.xpath('//div[@class="Cf_name"]/a/text()')
        #print(len(ratings))
        cntryCount=len(ratings)
        for rating in range(cntryCount):
            if rating==0:
                print("*****************  ODI RANKINGS  *****************")
                print("=================Batting Rankings===============")
            elif rating==10:
                print("==================Bowling Rankings================")
            elif rating==20:
                print("====================All-Rounder Rankings==============")
            elif rating==30:
                print("*****************  TEST RANKINGS  *****************")
                print("=================Batting Rankings===============")
            elif rating==40:
                print("==================Bowling Rankings================")
            elif rating==50:
                print("====================All-Rounder Rankings==============")
            elif rating==60:
                print("*****************  T20 RANKINGS  *****************")
                print("=================Batting Rankings===============")
            elif rating==70:
                print("==================Bowling Rankings================")
            elif rating==80:
                print("==================All-Rounder Rankings================")




            print(ratings[rating])
            
    else:
        print('No valid entry!')

#=====end of players ranking method======================
if __name__=='__main__':
    ratingType=raw_input('Which ICC rating you want to know? 1. Players 2. Team ')

    if ratingType!="":
        getUrls(ratingType)
    else:
        print('WTF!')







    
    
    
