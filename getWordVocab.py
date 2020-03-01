import requests
import json
from lxml import html
site_url = 'https://www.enchantedlearning.com/wordlist/{}'


def getwordvovab(word):
    siteurl = site_url.format(word)
    # print(siteurl)
    siteres = requests.get(siteurl)
    html_tree = html.fromstring(siteres.content)
    vocab = html_tree.xpath(
        '//*[@id="main-content"]/div/div/div[2]/div/div/text()')

    if len(vocab) > 0:
        print('Total words {} '.format(len(vocab)))
        print()
        for words in vocab:
            if(len(words) > 1):                 # ignoring the alphabet
                print(words)
    else:
        print('No vocab found for the word {} !')


if __name__ == '__main__':
    word = input('What word you are looking for? ')
    getwordvovab(word)
