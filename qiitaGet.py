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

def dctSortDesc(dct):
    for k, v in sorted(dct.items(), key=lambda x: -x[1]):
      print(str(k) + ": " + str(v))

def countArray(arrays):
    arrange = {}
    maxArray = len(arrays)
    i = 0
    tmp = ''
    before = ''
    j = 1
    for i in range(0,maxArray):
        tmp = arrays[i]
        if(tmp == before):
            j = j + 1
        else:
            arrange[before] = j
            j = 1
        before = arrays[i]
    return arrange

def rankGet(dct,rank):
    i = 0
    for key, value in dct.items():
        i += 1
        if i < rank:
          print('{}: {}'.format(key, value))
        else:
          return rank

accessToken = '6bc2c28ebed49f98070caab7668da51a16b1df0c'
client = super_QiitaClient(access_token=accessToken)
i = 0
maxArray = 20
ora = []
for i in range(1,maxArray):
    res = client.recentlist(str(i))
    ans = res.to_json()
    maxArrayLength = len(ans)
    j = 0
    for j in range(0,maxArrayLength):
     strOrigin = ans[j]["user"]["organization"]
     if strOrigin is not None and len(strOrigin) != 0:
         ora.append(strOrigin.encode('utf-8'))

ora2 = sorted(ora)
#print(ora2)
dic = {}
dic = countArray(ora2)
dic = dctSortDesc(dic)

#rank = rankGet(dic,10)
