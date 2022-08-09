
import requests
import time
import urllib, json
from bson import json_util
from pymongo import MongoClient
import json
import config
import collections

client = MongoClient("mongodb+srv://abcd:123@cluster0.eqdj4ze.mongodb.net/?retryWrites=true&w=majority")


db = client.mydb
records = db.mycl
   
while True:
    r = requests.get("https://api.wazirx.com/sapi/v1/tickers/24hr")
    if r.status_code == 200:
        data = r.json()
        print(data)
        records.insert_many(data)
        #records.insert_one(data)
        time.sleep(86400)
    else:
        exit()
        
