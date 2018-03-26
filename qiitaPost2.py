import sys
import requests
import json

qid = '9941d32feddeabdfde3a'
url = 'https://qiita.com/api/v2/items/' + qid

print(url)
#url = 'https://qiita.com/api/v2/items'
token = '6bc2c28ebed49f98070caab7668da51a16b1df0c'

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}
title = 'test!!!update!!!###body'
tags = 'test'
body = '###body###test'

tag_data = [{'name': tag} for tag in tags]
post_data = {
    'body': body,
    'title': title,
    #'tags': tag_data,
    #.'tweet' => True,
}

r = requests.patch(url, headers=headers, data=json.dumps(post_data))
print(r)
