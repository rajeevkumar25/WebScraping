import requests
from lxml import html

def getSiteContent(url):
    siteContent=requests.get(url)
    htmlTree=html.fromstring(siteContent.content)
    return htmlTree

def getDoctorsList(loc,doctype):
    if loc!="" and doctype!="":
        doctype=doctype.replace(" ","-")
        loc=loc.replace(" ","-")
        practoUrl='https://www.practo.com/pune/'+doctype+'/'+loc
        print(practoUrl)

    htmlTreePracto=getSiteContent(practoUrl)
    docNames=htmlTreePracto.xpath('//h2[contains(@data-qa-id,"doctor_name")]/text()')
    #docNames=htmlTreePracto.xpath('//div[@class="c-card-info"]/a/h2/text()')
    docDegree=htmlTreePracto.xpath('//div[@class="c-card-info"]/div/h3/text()')
    #docExp=htmlTreePracto.xpath('//h3[contains(@data-qa-id,"doctor_experience")]/span/text()')
    #docExp=htmlTreePracto.xpath('//h3[@data-qa-id="doctor_experience"]/span/@data-reactid')
    #print(len(docNames))
    docDetails=zip(docNames,docDegree)

    for doc in docDetails:
        print(doc)
    
if __name__=='__main__':
    getDoctorsList('pimple gurav','dentist')
