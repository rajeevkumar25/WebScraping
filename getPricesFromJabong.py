import requests
from lxml import html

def getSiteContent(url):
    siteContent=requests.get(url)
    htmlTree=html.fromstring(siteContent.content)
    #print(htmlTree.xpath('//*[@id="search"]/div/h1/text()'))
    return htmlTree


def getItemPrice(itemName,brand):
    itemName=itemName.replace(" ","-")
    brand=brand.replace(" ","%20")

    #mynatraItemUrl='https://www.myntra.com/men-'+brand+'-'+itemName+'?f=&sort=low'
    mynatraItemUrl='https://www.jabong.com/men-'+itemName+'?f=Brand%3A'+brand+'%3A%3AGlobal%20Size%3A42%2C44'+'&sort=price_asc'
    
                   
    print(mynatraItemUrl)
    htmlTreeMyntra=getSiteContent(mynatraItemUrl)
    prdLink=prdLink=htmlTreeMyntra.xpath('//div[@class="col-xxs-6 col-xs-4 col-sm-4 col-md-3 col-lg-3 product-tile img-responsive"]/a/div/div/span/text()')
    print(type(prdLink))
    for prd in prdLink:
        print(prd)

if __name__=='__main__':
    #getItemPrice('casual shirt','Peter England')
    item=raw_input('Please enter item name-  ')
    brand=raw_input('Please enter brand-  ')

    if(item!="" and brand!=""):
        getItemPrice(item,brand)