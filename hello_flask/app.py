import datetime
from email.headerregistry import HeaderRegistry
import json
from flask import render_template
from flask import Flask
import requests
import time
import pandas as pd
from tabulate import tabulate
from pymongo import MongoClient
import requests
import time
from pymongo import MongoClient
import pandas as pd

app = Flask(__name__)
#******************************html page ***************************

@app.route("/")
def home():
    return render_template("home.html")

 
# New functions
@app.route("/graph")
def graph():
    toadd= {'QuoteAssets':{ 'Average_highPrice':'Average High Price','Average_lowPrice':'Average Low Price'}}
    client = MongoClient("mongodb+srv://abcd:123@cluster0.eqdj4ze.mongodb.net/?retryWrites=true&w=majority")
    db = client.mydb
    records = db.mycl
    one_record =records.find_one()
    all_records = records.find()
    dict1=all_records
    list_cursor =list(all_records)
    df =pd.DataFrame(list_cursor)
    af=df
    af.pop('_id')
    af.pop('askPrice')
    af.pop('baseAsset')
    af.pop('bidPrice')
    af.pop('volume')
    af.pop('at')
    af["highPrice"] = pd.to_numeric(af["highPrice"], downcast="float")
    af["lowPrice"] = pd.to_numeric(af["lowPrice"], downcast="float")
    avg=af.groupby('quoteAsset')[['highPrice', 'lowPrice']].agg('mean')
    avg["highPrice"] = avg["highPrice"].astype(str)
    avg["lowPrice"] = avg["lowPrice"].astype(str)
    avg = avg.rename(columns={'lowPrice': 'Average_lowPrice', 'highPrice': 'Average_highPrice'})
    dict = avg.to_dict('index')
    toadd.update(dict)
    return render_template("graph.html",data=toadd)
client = MongoClient("mongodb+srv://abcd:123@cluster0.eqdj4ze.mongodb.net/?retryWrites=true&w=majority")
db = client.mydb
records = db.mycl
one_record =records.find_one()
all_records = records.find()
dict1=all_records
list_cursor =list(all_records)
df =pd.DataFrame(list_cursor)
print(df)
af=df
af.pop('_id')
af.pop('askPrice')
af.pop('baseAsset')
af.pop('bidPrice')
af.pop('volume')
af.pop('at')
print(af)
af["highPrice"] = pd.to_numeric(af["highPrice"], downcast="float")
af["lowPrice"] = pd.to_numeric(af["lowPrice"], downcast="float")
avg=af.groupby('quoteAsset')[['highPrice', 'lowPrice']].agg('mean')
avg["highPrice"] = avg["highPrice"].astype(str)
avg["lowPrice"] = avg["lowPrice"].astype(str)
avg = avg.rename(columns={'lowPrice': 'Average_lowPrice', 'highPrice': 'Average_highPrice'})
print(avg)

if __name__=='__main_':
    app.run()
