#NSE
import csv
import requests as s
import pandas as pd

def extract():
    #COL=["STK","EXP","NIFTY","SYMBOL","OI","CHNGOI","OICHNGPER","TTV","IV","LTP","CHNG","PCHNG","TBQ","TSQ","BQ","BP","AQ","AP","SPOT"]
    #with requests as s:
    url = "https://www.nseindia.com/api/equity-stockIndices?csv=true&index=NIFTY%2050"
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36','accept-language':'en-IN,en;q=0.9,bn;q=0.8','accept-encoding':'gzip, deflate, br'}
    download = s.urlopen(url)
"""
    dc = download.content.decode("utf-8")
    #file = open("n50","a+")
    cr = csv.reader(dc.splitlines(),delimiter = ",")
    l = list(cr)
    for i in l:
        print(i)



"""
extract()
