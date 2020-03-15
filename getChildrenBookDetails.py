# Gets the books recommendation from 6 to 10 year old children and dumps into a csv file
import requests
import time
from bs4 import BeautifulSoup as bsoup
import csv

siteurl = 'https://www.indiabookstore.net/categories/age6To10'
sitemainurl = 'https://www.indiabookstore.net/'


class getBookDetails():

    def __init__(self, siteurl, sitemainurl):
        self.siteurl = siteurl
        self.sitemainurl = sitemainurl

    # this metod will get the books name along with the author name
    def getBookName(self):
        site_res = requests.get(self.siteurl)
        print(site_res.status_code)
        if site_res.status_code == 200:

            soup_content = bsoup(site_res.content, 'html.parser')
            bookname = soup_content.find_all(class_='truncateName')
            with open('books_data.csv', mode='w', encoding='utf8') as bookfile:
                csv_writer = csv.writer(bookfile)
                for item in bookname:
                    csv_writer.writerow(item)
            #    print(item.text)

    def searchBooks(self):
        topic = input('Which topic book you are looking for?')
        searchurl = self.sitemainurl+'search?q='+topic
        print(searchurl)
        search_res = requests.get(searchurl)
        print(search_res.content)
        print(search_res.status_code)
        if search_res.status_code == 200:
            soupsearch_content = bsoup(search_res.content, 'html.parser')
            # print(soupsearch_content)
            # time.sleep(5)
            booklist = soupsearch_content.find_all(class_='bookDetailsLink')
            for book in booklist:
                print(book)


clsobj = getBookDetails(siteurl, sitemainurl)
clsobj.getBookName()
# clsobj.searchBooks()
