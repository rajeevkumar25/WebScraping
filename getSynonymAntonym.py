# This program will get synonyms or antonyms of a word from http://api.datamuse.com/ API
# which can be invoked without any auth

import requests
import json


apiu_url = 'http://api.datamuse.com/words?rel_{}={}'


def getSynonym(word):
    api_res = requests.get(apiu_url.format('syn', word))
    res = api_res.json()

    for item in res:
        print(item['word'])


def getAntonym(word):
    api_res = requests.get(apiu_url.format('ant', word))
    res = api_res.json()

    for item in res:
        print(item['word'])


if __name__ == '__main__':
    word = input('Please enter the word - ')

    whattofind = input(
        'Do you want to know Synonyms or Antonyms? Type ''S'' or ''A'' - ')
    if (whattofind.capitalize() == 'S'):
        getSynonym(word)
    if (whattofind.capitalize() == 'A'):
        getAntonym(word)
