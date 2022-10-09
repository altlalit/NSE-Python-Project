

# Extract Index Data

symbol = ['NIFTY SMLCAP 100','NIFTY SMLCAP 250','NIFTY SMLCAP 50','NIFTY MIDCAP 150','NIFTY 50','NIFTY NEXT 50','NIFTY FMCG']
td = date.today().strftime("%Y/%m/%d")
a = td.split("/")
y = int(a[0])
m = int(a[1])
d = int(a[2])
"""
data1=[]
data1 = pd.DataFrame(data1)
for x in symbol:
    data = get_history(symbol=x, start=date(y,m,d-5), end=date(y,m,d), index = True)
    data = pd.DataFrame(data)
    data['Index_Name'] = x
    data1 = pd.concat([data1,data])
    print(x)

# Save Index Data
data1.to_csv('Index_Data.csv', index=True)
"""
# Extract Company Data
symbol =  ['CIPLA','BPCL','SUNPHARMA','JSWSTEEL','IOC','DRREDDY','POWERGRID','COALINDIA','ITC','TITAN','DIVISLAB','SHREECEM','GRASIM','ASIANPAINT','ONGC','BAJAJFINSV','SBIN','BAJFINANCE','HEROMOTOCO','SBILIFE','KOTAKBANK','HDFCBANK','ICICIBANK','TECHM','HCLTECH','BAJAJ-AUTO','RELIANCE','UPL','LT','INFY','HDFC','HINDUNILVR','EICHERMOTO','WIPRO','TATAMOTORS','INDUSINDBK','BHARTIARTL','TCS','AXISBANK','HDFCLIFE','ULTRAACEMCO','ADANIPORTS','M&M','BRITANNIA','TATASTEEL','NTPC','HINDALCO','TATACONSUM','MARUTI','NESTLEIND']

data1=[]
data1 = pd.DataFrame(data1)
counter = 0
for x in symbol:
    data = get_history(symbol=x, start=date(y,m,d-1), end=date(y,m,d))
    data = pd.DataFrame(data)
    data1 = pd.concat([data1,data])
    print(x)
    

print()
print()
print("Success !!!")

# Save Company Data
data1.to_csv('Company_Data.csv', index=True,mode="a")
