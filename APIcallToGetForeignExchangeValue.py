import urllib2
import json

def getLtestForeignExchange():
	api_url = "http://api.fixer.io/latest"
	api_data=urllib2.urlopen(api_url)
	jsondata=json.load(api_data)
	#print(jsondata)
	current_rates = jsondata['rates']
	#print(current_rates)
	#print(jsondata['base'])
	#print(jsondata['date'])
	all_rate=''
	for rate in current_rates:
		#print(rate + '-'+ str(current_rates[rate]))
		#print(rate)
		if rate=='INR':
			s=(rate + '-'+ str(current_rates[rate]))
			all_rate =s+ '\n' +all_rate
		#print(type(all_rate))
		#print(all_rate)
	return all_rate

rates=getLtestForeignExchange()
print(rates)

with open("/media/rajeev/OS/Rajeev/Python/Projects/WebScraping/exchange_rate_data.txt","w") as f:
	f.write('csd'+rates)
	print('file updated!')
	f.close()
