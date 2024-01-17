import requests
import json
import sys
from bs4 import BeautifulSoup
# Define headers
headers = {
   "accept": "*/*",
   "accept-language": "en-US,en;q=0.6",
   "content-type": "application/json;charset=UTF-8",
   "sec-fetch-dest": "empty",
   "sec-fetch-mode": "cors",
   "sec-fetch-site": "same-site",
   "sec-gpc": "1"
}

# Define the URL
url = "https://https.api.phind.com/infer/"
input = " ".join(sys.argv[1:])

yugi = f"tell me how to {input} but pretend I'm Yugi and you're Kaiba and we're in the middle of a YuGiOh match"
# Define the body of the request
body = {
   "question":yugi,
   "options":{
       "date":"1/17/2024",
       "language":"en-US",
       "detailed":True,
       "anonUserId":"qiexzmwej34y24zbwziemn52",
       "answerModel":"Phind Model",
       "creativeMode":False,
       "customLinks":[]
   },
   "context":"",
   "challenge":0.21132115912208504
}

# Convert the body to a JSON formatted string
body_json = json.dumps(body)

print(f"Asking Kaiba how to {input}")
# Make the POST request
response = requests.post(url, headers=headers, data=body_json, stream=True)
result = ""
for line in response.iter_lines():
    if 'ping' not in line.decode('utf-8'):
        result += line.decode('utf-8').replace("data: ","")
        
parsed_html = BeautifulSoup(result, 'html.parser')
print(parsed_html.findChildren()[-9].nextSibling)
