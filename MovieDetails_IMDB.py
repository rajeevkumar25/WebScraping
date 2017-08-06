from bs4 import BeautifulSoup as soup
import requests
import json
imdb_base_url="http://www.imdb.com/title"

def getMovieDetails(html):
    data={}
    data['title']=html.find(itemprop='name').text.strip()
    data['description']=html.find(itemprop='description').text.strip()
    data['rating']=html.find(itemprop='ratingValue').text

    tags=html.findAll(itemprop="actors")
    actors=[]
    for actor in tags:
        actors.append(actor.text.strip())
    data['cast']=actors

    #print(data['title'])
    #print("Rating-" + data['rating'])
    #print(data['description'])
    #print(data['cast'])
    json_data=json.dumps(data)
    print(json_data)
    

def getHtml(url):
    html_response=requests.get(url)
    return soup(html_response.content,'html.parser')

def SearchGoogle(movieName):
    html = getHtml('https://www.google.co.in/search?q='+movieName)
    for cite in html.findAll('cite'):
        if 'imdb.com/title/tt' in cite.text:
            html=getHtml('http://'+cite.text)
            break
    
    #print(html)
    return getMovieDetails(html)
  
if __name__=='__main__':
    movie_name=raw_input('Please enter movie name:')

    if movie_name!="":
        SearchGoogle(movie_name)
    else:
        print("Invalid Movie Name!")






