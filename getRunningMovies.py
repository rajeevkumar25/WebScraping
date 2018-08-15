import requests
from lxml import html

bookmyshow_url='https://in.bookmyshow.com/pune/movies/'

def getRunningMovies(lang):
    if (lang.lower()=='hindi' or 'english'):
        new_url=bookmyshow_url+lang+'/'
    else:
        new_url=bookmyshow_url
    bookmyshow_content=requests.get(new_url)

    html_tree=html.fromstring(bookmyshow_content.content)
    #movies=html_tree.xpath('//*[@id="now-showing"]/section[1]/div/div/div[2]/div/div/div[1]/div[1]/a/div/div[2]/div[2]/div[1]/h4/text()')
    movies=html_tree.xpath('//div[@class="card-title"]/h4/text()')
    movie_count=len(movies)
    if movie_count>0:
        for movie in range(movie_count):
            print(movies[movie])
    else:
        print('Oops ! Sorry no movies found!')
    

if __name__=='__main__':
    language=raw_input('Which language movies? ')
    if language!="":
        getRunningMovies(language)
    else:
        print('Displaying English and Hindi both')
        getRunningMovies('both')