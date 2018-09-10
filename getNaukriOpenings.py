from lxml import html
import requests as req

def getOpenings(role):
    baseURl='https://www.naukri.com/'

    naukriURL=baseURl+role+'-jobs-in-pune'

    naukriSiteContent=req.get(naukriURL)
    htmlTree=html.fromstring(naukriSiteContent.content)

    
    openingComps=htmlTree.xpath('//span[@class="org"]/text()')
    skills=htmlTree.xpath('//span[@class="skill"]/text()')
    shortDesc=htmlTree.xpath('//span[@class="desc"]/text()')
    exp=htmlTree.xpath('//span[@class="exp"]/text()')
    compSkills=zip(openingComps,skills,exp,shortDesc)
    
    if len(compSkills)>0:
        for opening in compSkills:
            print('                                               ')
            print(opening)
            print('                                               ')
            print('===============================================')
        
    else:
        print('Oops ! No Openings !!')


if __name__=='__main__':
    role=raw_input('Please enter role/postion - ')
    if(len(role)>1):
        roleText=role.replace(" ","-")
        getOpenings(roleText)
    else:
        getOpenings(role)
