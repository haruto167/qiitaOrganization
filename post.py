import urllib.request
import json

qid = '0c9234d6ef77f3a5a09c'
url = 'https://qiita.com/api/v2/items/{}'.format(qid)
#url = 'https://qiita.com/api/v2/items/'
accessToken='ada592c7254cd9e768147d9a1236c1e38104fb2e'
obj = {"body" : "### aaaaa", "title": "Example title"}
headers = {'Authorization': 'Bearer {}'.format(accessToken), "Content-Type" : "application/json"}

obj = {"body" : "### aaaaa"} 
json_data = json.dumps(obj).encode("utf-8")
try:
   request = urllib.request.Request(url,data=json_data,method="POST",headers=headers)
except urllib.error.HTTPError as err:
   print('--------') 
   print(err)
   
response = urllib.request.urlopen(request)
html = response.read()

