import requests
import json 

url = 'http://api.nbp.pl/api/exchangerates/tables/A/'
r = requests.get(url)
print(f"Code status: {r.status_code}")

#analysing data structure 
response_dict = r.json()
readable_file = 'data/readable_nbp_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
