import numpy as np
from qiita_v2.client import QiitaClient
from datetime import datetime as dt
from dateutil import relativedelta

def getLastWeek(i):
   now = dt.now()
   lastweek = now - relativedelta.relativedelta(weeks=i)
   strdate = dt.strftime(lastweek, '%Y-%m-%d')
   return strdate

#Extends
#Use Qiita API
class super_QiitaClient(QiitaClient):
    def recentlist(self, id, params=None, headers=None):
        geturl = "/items?page={}&per_page=100&query=created%3A>" + getLastWeek(1)
        return self.get(geturl.format(id), params, headers)

def ranksort(data):
    return sorted(data.items(), key=lambda item: item[1])

accessToken = '6bc2c28ebed49f98070caab7668da51a16b1df0c'
client = super_QiitaClient(access_token=accessToken)
target = {}
i = 0
maxArray = 20 
for i in range(1,maxArray):
    res = client.recentlist(str(i))
    ans = res.to_json()
    maxArrayLength = len(ans)
    j = 0
    for j in range(0,maxArrayLength):
     #print(j)
     #nt(ans[j]["id"])
     strOrigin = ans[j]["user"]["organization"]
     if strOrigin is not None and len(strOrigin) != 0:
         print(ans[j]["id"])
         print(strOrigin.encode('utf-8')) 
         #f = open('test.txt','a')
         #f.write(str(strOrigin)  + '\n')
         #f.close()
     #print(strOrigin)
     #print(strorigin.encode('utf-8'/))
     #target[ans[j]["id"]] = ans[j]["likes_count"]


#print(ranksort(target))

