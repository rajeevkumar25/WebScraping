from bs4 import BeautifulSoup as soup
import requests

adder_toprated_url = 'http://www.adder.tv/shows?order=rating'
adder_mostpopular_url = 'http://www.adder.tv/shows?order=popular'
adder_base_url = 'www.adder.tv'

def getBestRatedTvShows(url):

	try:
		url_response=requests.get(url)
		if url_response.status_code==200:
			url_content=url_response.text
			url_soup=soup(url_content,'html.parser')
			#print(url_soup.title.text)
			show_names=url_soup.findAll('div',{'class':'details'})

			for name in show_names:
				print(name.a.text + '-' + name.span.text)
				print('Download Link-'+ adder_base_url+name.a['href'])
				print(name.p.text)
				print('====================================')
		else:
			print(url_response.status_code)

	except:
		print(url)
		print('Some exception')
		
if __name__=='__main__':
	print('1: Top Rated')
	print('2:Most Popular')

	url_number=input()
	if url_number==1:
		url=adder_toprated_url
	elif url_number==2:
		url=adder_mostpopular_url
	elif url_number>2:
		print('wrong input,enter again')
		url_number=input()
	else:
		print('wrong input!')
		exit
	

	getBestRatedTvShows(url)

