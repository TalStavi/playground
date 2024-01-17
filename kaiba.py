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

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# Define the URL
url = "https://https.api.phind.com/infer/"
input = " ".join(sys.argv[1:])

yugi = f"Tell me how to {input} but pretend I'm Yugi and you are Seto Kaiba and we're in the middle of a YuGiOh match but you're stopping eveyrthing to tell me in a dramatic way how to do it anyway, give YuGiOh examples and references if possible."
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
print(parsed_html.findChildren()[-9].nextSibling.replace(r"```bash", " " + color.GREEN)
      .replace(r"```", color.END+ " ")
      .replace(r" `", " " +color.GREEN)
      .replace(r"` ", color.END+ " ")
      .replace(r"`.", color.END + ". "))
