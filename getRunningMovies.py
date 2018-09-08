import requests
from lxml import html
from getMovieIMDBRating import getMovieIMDBRating

bookmyshow_url='https://in.bookmyshow.com/pune/movies/'

def getRunningMovies(lang):
    if (lang.lower()=='hindi' or 'english'):
        new_url=bookmyshow_url+lang+'/'
    else:
        new_url=bookmyshow_url
    bookmyshow_content=requests.get(new_url)

    html_tree=html.fromstring(bookmyshow_content.content)
    movies=html_tree.xpath('//div[@class="card-title"]/h4/text()')
    movie_count=len(movies)
    if movie_count>0:
        for movie in range(movie_count):
            print(movies[movie])
            rating=getMovieIMDBRating(movies[movie])
            print(rating)
    else:
        print('Oops ! Sorry no movies found!')
    

if __name__=='__main__':
    language=raw_input('Which language movies? ')
    if language!="":
        getRunningMovies(language)
    else:
        print('Displaying English and Hindi both')
        getRunningMovies('both')