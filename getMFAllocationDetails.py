import requests
import pandas as pd

import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'accept-version': '7.0.0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
}

response = requests.get('https://api.tickertape.in/mutualfunds/M_QUNB/holdings', headers=headers)
response_json=response.json()

#print(response_json['data']['currentAllocation'][0]['title'])
allocations=response_json['data']['currentAllocation']
print(allocations)
allocations=response_json['data']['currentAllocation']
master_list=[]

for item in allocations:

    itemdetails={}
    itemdetails['type']=item['type']
    itemdetails['title']=item['title']
    itemdetails['latest']=item['latest']
    master_list.append(itemdetails)

data=pd.DataFrame(master_list)
print(data)





