import requests
from lxml import html

#next- write a method to get an option from the user for topic of thr quote and get then get quotes
# like for topic family URL is - https://www.brainyquote.com/topics/family

brainyUrl='https://www.brainyquote.com/topics/wisdom'

def getSiteContent(url):
    siteContent=requests.get(url)
    htmlTree=html.fromstring(siteContent.content)
    return htmlTree

def getWisdomQuotes():
    htmlTree=getSiteContent(brainyUrl)
    quotes=htmlTree.xpath('//div[@class="clearfix"]/a[1]/text()')
    #print(quotes)
    authors=htmlTree.xpath('//div[@class="clearfix"]/a[2]/text()')
    #print(authors)
    if len(authors)!=0:
        wisdoms=zip(quotes,authors)
    else:
        wisdoms=quotes    
    #print(len(wisdoms))
    for wisdom in wisdoms:
        print(wisdom)
        print('============================================')
def getTopicWisdom(topic):
    topicUrl='https://www.brainyquote.com/topics/'+topic
    htmlTree=getSiteContent(topicUrl)
    
    topicQuotes=htmlTree.xpath('//div[@class="clearfix"]/a[1]/text()')
    topicQuoteAuthors=htmlTree.xpath('//div[@class="clearfix"]/a[2]/text()')
    if len(topicQuoteAuthors)!=0:
        topicWisdom=zip(topicQuotes,topicQuoteAuthors)
    else:
        topicWisdom=topicQuotes    
    #print(len(topicWisdom))
    if (len(topicWisdom))>0:
        for wis in topicWisdom:
            print(wis)
            print('============================================')
    else:
        print('NoQuotesFound!')

if __name__=='__main__':
    wisdomType=input('Which Quotes? Random or Topic ! ')

    if wisdomType.lower()=='random':
        getWisdomQuotes()
    elif wisdomType.lower()=='topic':
        topic=input('Which Topic? (Ex. Family , Brainy , Funny , Money, Mom , Respect , Sad , Motivational , Time, Trust etc.')
        if topic.lower()!="":
            getTopicWisdom(topic)
        