import requests
import time
import os
import pandas as pd
from datetime import datetime
import shutil
TOTAL_TARDING_MINUTES=375
INTERVAL=2                    #<<<<====================CHANE ACCORDINGLY[1/3/5/10/15...............]
REPEAT_CODE=TOTAL_TARDING_MINUTES/INTERVAL
EXPDATE='17-03-2022'
STK1=15800
STK2=15850
STK3=15900
STK4=15950
STK5=16000
STK6=16050
STK7=16100
STK8=16150
STK9=16200
STK10=16250
STK11=16300
STK12=16350
STK13=16400
STK14=16450
STK15=16500
STK16=16550
STK17=16600
STK18=16650
STK19=16700
STK20=16750
STK21=16800
STK22=16850
STK23=16900
STK24=16950
STK25=17000
STK26=17050
STK27=17100
def DATA_EXTRACT():
    symbolce1="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK1)+str(".00")    
    symbolce2="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK2)+str(".00")     
    symbolce3="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK3)+str(".00")     
    symbolce4="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK4)+str(".00")     
    symbolce5="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK5)+str(".00")     
    symbolce6="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK6)+str(".00")     
    symbolce7="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK7)+str(".00")
    symbolce8="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK8)+str(".00")
    symbolce9="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK9)+str(".00")     
    symbolce10="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK10)+str(".00")     
    symbolce11="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK11)+str(".00")     
    symbolce12="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK12)+str(".00")
    symbolce13="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK13)+str(".00")
    symbolce14="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK14)+str(".00")    
    symbolce15="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK15)+str(".00")     
    symbolce16="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK16)+str(".00")     
    symbolce17="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK17)+str(".00")     
    symbolce18="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK18)+str(".00")     
    symbolce19="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK19)+str(".00")     
    symbolce20="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK20)+str(".00")
    symbolce21="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK21)+str(".00")
    symbolce22="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK22)+str(".00")     
    symbolce23="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK23)+str(".00")     
    symbolce24="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK24)+str(".00")     
    symbolce25="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK25)+str(".00")
    symbolce26="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK26)+str(".00")
    symbolce27="OPTIDXNIFTY"+str(EXPDATE)+"CE"+str(STK27)+str(".00")
    #--------------------------------------------------------------------------
    symbolpe1="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK1)+str(".00")
    symbolpe2="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK2)+str(".00")
    symbolpe3= "OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK3)+str(".00")
    symbolpe4="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK4)+str(".00")
    symbolpe5= "OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK5)+str(".00")
    symbolpe6="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK6)+str(".00")
    symbolpe7="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK7)+str(".00")
    symbolpe8="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK8 )+str(".00")
    symbolpe9="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK9)+str(".00")
    symbolpe10= "OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK10)+str(".00")
    symbolpe11="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK11)+str(".00")
    symbolpe12="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK12)+str(".00")
    symbolpe13="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK13 )+str(".00")
    symbolpe14="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK14)+str(".00")
    symbolpe15="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK15)+str(".00")
    symbolpe16= "OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK16)+str(".00")
    symbolpe17="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK17)+str(".00")
    symbolpe18= "OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK18)+str(".00")
    symbolpe19="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK19)+str(".00")
    symbolpe20="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK20)+str(".00")
    symbolpe21="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK21 )+str(".00")
    symbolpe22="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK22)+str(".00")
    symbolpe23= "OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK23)+str(".00")
    symbolpe24="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK24)+str(".00")
    symbolpe25="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK25)+str(".00")
    symbolpe26="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK26 )+str(".00")
    symbolpe27="OPTIDXNIFTY"+str(EXPDATE)+"PE"+str(STK27 )+str(".00")
    #--------------------------------------------------------------------------
    COL=["STK","EXP","NIFTY","SYMBOL","OI","CHNGOI","OICHNGPER","TTV","IV","LTP","CHNG","PCHNG","TBQ","TSQ","BQ","BP","AQ","AP","SPOT"]
    url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
         'accept-language':'en-US,en;q=0.9,bn;q=0.8','accept-encoding':'gzip, deflate, br'}
    r=requests.get(url,headers=headers).json()
    data=r["filtered"]["data"]
    df=pd.DataFrame(data)
    df.to_csv("RAW_DATA.csv",index=False)
    ndf=pd.read_csv("RAW_DATA.csv")
    rows=len(ndf)
    for i in range(0,rows):
        STKCE=ndf["CE"].iloc[i]
        STKCE=eval(STKCE)
        STKPE=ndf["PE"].iloc[i]
        STKPE=eval(STKPE)
        CEDF=pd.DataFrame(STKCE,index=[0])
        PEDF=pd.DataFrame(STKPE,index=[0])
        CEDF.to_csv("FILTERED_DATA.csv",index=False,mode='a',header=False)
        PEDF.to_csv("FILTERED_DATA.csv",index=False,mode='a',header=False)
    final=pd.read_csv("FILTERED_DATA.csv")
    final.columns=COL
    final.to_csv("FILTERED_DATA.csv",index=False)
    #os.system('copy FILTERED_DATA.csv LIVE_DATA.csv')
    shutil.copy('FILTERED_DATA.csv','LIVE_DATA.csv')
    os.remove('FILTERED_DATA.csv')
    os.remove('RAW_DATA.csv')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    ce1_ltp=final["LTP"][(final.SYMBOL==symbolce1)].to_string(index=False)
    ce1_iv=final["IV"][(final.SYMBOL==symbolce1)].to_string(index=False)
    ce1_oi=final["OI"][(final.SYMBOL==symbolce1)].to_string(index=False)
    ce1_ttv=final["TTV"][(final.SYMBOL==symbolce1)].to_string(index=False)
    ce1_choi=final["CHNGOI"][(final.SYMBOL==symbolce1)].to_string(index=False)
    
    ce1_stk=final["STK"][(final.SYMBOL==symbolce1)].to_string(index=False)      
    ce2_stk=final["STK"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    ce3_stk=final["STK"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    ce4_stk=final["STK"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    ce5_stk=final["STK"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    ce6_stk=final["STK"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    ce7_stk=final["STK"][(final.SYMBOL==symbolce7)].to_string(index=False)
    ce8_stk=final["STK"][(final.SYMBOL==symbolce8)].to_string(index=False)     
    ce9_stk=final["STK"][(final.SYMBOL==symbolce9)].to_string(index=False)     
    ce10_stk=final["STK"][(final.SYMBOL==symbolce10)].to_string(index=False)     
    ce11_stk=final["STK"][(final.SYMBOL==symbolce11)].to_string(index=False)     
    ce12_stk=final["STK"][(final.SYMBOL==symbolce12)].to_string(index=False)
    ce13_stk=final["STK"][(final.SYMBOL==symbolce13)].to_string(index=False)
    ce14_stk=final["STK"][(final.SYMBOL==symbolce14)].to_string(index=False)      
    ce15_stk=final["STK"][(final.SYMBOL==symbolce15)].to_string(index=False)     
    ce16_stk=final["STK"][(final.SYMBOL==symbolce16)].to_string(index=False)     
    ce17_stk=final["STK"][(final.SYMBOL==symbolce17)].to_string(index=False)     
    ce18_stk=final["STK"][(final.SYMBOL==symbolce18)].to_string(index=False)     
    ce19_stk=final["STK"][(final.SYMBOL==symbolce19)].to_string(index=False)     
    ce20_stk=final["STK"][(final.SYMBOL==symbolce20)].to_string(index=False)
    ce21_stk=final["STK"][(final.SYMBOL==symbolce21)].to_string(index=False)     
    ce22_stk=final["STK"][(final.SYMBOL==symbolce22)].to_string(index=False)     
    ce23_stk=final["STK"][(final.SYMBOL==symbolce23)].to_string(index=False)     
    ce24_stk=final["STK"][(final.SYMBOL==symbolce24)].to_string(index=False)     
    ce25_stk=final["STK"][(final.SYMBOL==symbolce25)].to_string(index=False)
    ce26_stk=final["STK"][(final.SYMBOL==symbolce26)].to_string(index=False)
    ce27_stk=final["STK"][(final.SYMBOL==symbolce27)].to_string(index=False)    

    pe1_stk=final["STK"][(final.SYMBOL==symbolpe1)].to_string(index=False)      
    pe2_stk=final["STK"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    pe3_stk=final["STK"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    pe4_stk=final["STK"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    pe5_stk=final["STK"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    pe6_stk=final["STK"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    pe7_stk=final["STK"][(final.SYMBOL==symbolpe7)].to_string(index=False)
    pe8_stk=final["STK"][(final.SYMBOL==symbolpe8)].to_string(index=False)   
    pe9_stk=final["STK"][(final.SYMBOL==symbolpe9)].to_string(index=False)     
    pe10_stk=final["STK"][(final.SYMBOL==symbolpe10)].to_string(index=False)     
    pe11_stk=final["STK"][(final.SYMBOL==symbolpe11)].to_string(index=False)     
    pe12_stk=final["STK"][(final.SYMBOL==symbolpe12)].to_string(index=False)
    pe13_stk=final["STK"][(final.SYMBOL==symbolpe13)].to_string(index=False)
    pe14_stk=final["STK"][(final.SYMBOL==symbolpe14)].to_string(index=False)      
    pe15_stk=final["STK"][(final.SYMBOL==symbolpe15)].to_string(index=False)     
    pe16_stk=final["STK"][(final.SYMBOL==symbolpe16)].to_string(index=False)     
    pe17_stk=final["STK"][(final.SYMBOL==symbolpe17)].to_string(index=False)     
    pe18_stk=final["STK"][(final.SYMBOL==symbolpe18)].to_string(index=False)     
    pe19_stk=final["STK"][(final.SYMBOL==symbolpe19)].to_string(index=False)     
    pe20_stk=final["STK"][(final.SYMBOL==symbolpe20)].to_string(index=False)
    pe21_stk=final["STK"][(final.SYMBOL==symbolpe21)].to_string(index=False)   
    pe22_stk=final["STK"][(final.SYMBOL==symbolpe22)].to_string(index=False)     
    pe23_stk=final["STK"][(final.SYMBOL==symbolpe23)].to_string(index=False)     
    pe24_stk=final["STK"][(final.SYMBOL==symbolpe24)].to_string(index=False)     
    pe25_stk=final["STK"][(final.SYMBOL==symbolpe25)].to_string(index=False)
    pe26_stk=final["STK"][(final.SYMBOL==symbolpe26)].to_string(index=False)
    pe27_stk=final["STK"][(final.SYMBOL==symbolpe27)].to_string(index=False)
    
    ce2_ltp=final["LTP"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    ce2_iv=final["IV"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    ce2_oi=final["OI"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    ce2_ttv=final["TTV"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    ce2_choi=final["CHNGOI"][(final.SYMBOL==symbolce2)].to_string(index=False)     
    
    ce3_ltp=final["LTP"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    ce3_iv=final["IV"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    ce3_oi=final["OI"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    ce3_ttv=final["TTV"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    ce3_choi=final["CHNGOI"][(final.SYMBOL==symbolce3)].to_string(index=False)     
    
    ce4_ltp=final["LTP"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    ce4_iv=final["IV"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    ce4_oi=final["OI"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    ce4_ttv=final["TTV"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    ce4_choi=final["CHNGOI"][(final.SYMBOL==symbolce4)].to_string(index=False)     
    
    ce5_ltp=final["LTP"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    ce5_iv=final["IV"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    ce5_oi=final["OI"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    ce5_ttv=final["TTV"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    ce5_choi=final["CHNGOI"][(final.SYMBOL==symbolce5)].to_string(index=False)     
    
    ce6_ltp=final["LTP"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    ce6_iv=final["IV"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    ce6_oi=final["OI"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    ce6_ttv=final["TTV"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    ce6_choi=final["CHNGOI"][(final.SYMBOL==symbolce6)].to_string(index=False)     
    
    ce7_ltp=final["LTP"][(final.SYMBOL==symbolce7)].to_string(index=False)     
    ce7_iv=final["IV"][(final.SYMBOL==symbolce7)].to_string(index=False)     
    ce7_oi=final["OI"][(final.SYMBOL==symbolce7)].to_string(index=False)     
    ce7_ttv=final["TTV"][(final.SYMBOL==symbolce7)].to_string(index=False)     
    ce7_choi=final["CHNGOI"][(final.SYMBOL==symbolce7)].to_string(index=False)     

    ce8_ltp=final["LTP"][(final.SYMBOL==symbolce8)].to_string(index=False)     
    ce8_iv=final["IV"][(final.SYMBOL==symbolce8)].to_string(index=False)     
    ce8_oi=final["OI"][(final.SYMBOL==symbolce8)].to_string(index=False)     
    ce8_ttv=final["TTV"][(final.SYMBOL==symbolce8)].to_string(index=False)     
    ce8_choi=final["CHNGOI"][(final.SYMBOL==symbolce8)].to_string(index=False)     

    ce9_ltp=final["LTP"][(final.SYMBOL==symbolce9)].to_string(index=False)     
    ce9_iv=final["IV"][(final.SYMBOL==symbolce9)].to_string(index=False)     
    ce9_oi=final["OI"][(final.SYMBOL==symbolce9)].to_string(index=False)     
    ce9_ttv=final["TTV"][(final.SYMBOL==symbolce9)].to_string(index=False)     
    ce9_choi=final["CHNGOI"][(final.SYMBOL==symbolce9)].to_string(index=False)     

    ce10_ltp=final["LTP"][(final.SYMBOL==symbolce10)].to_string(index=False)     
    ce10_iv=final["IV"][(final.SYMBOL==symbolce10)].to_string(index=False)     
    ce10_oi=final["OI"][(final.SYMBOL==symbolce10)].to_string(index=False)     
    ce10_ttv=final["TTV"][(final.SYMBOL==symbolce10)].to_string(index=False)     
    ce10_choi=final["CHNGOI"][(final.SYMBOL==symbolce10)].to_string(index=False)     

    ce11_ltp=final["LTP"][(final.SYMBOL==symbolce11)].to_string(index=False)     
    ce11_iv=final["IV"][(final.SYMBOL==symbolce11)].to_string(index=False)     
    ce11_oi=final["OI"][(final.SYMBOL==symbolce11)].to_string(index=False)     
    ce11_ttv=final["TTV"][(final.SYMBOL==symbolce11)].to_string(index=False)     
    ce11_choi=final["CHNGOI"][(final.SYMBOL==symbolce11)].to_string(index=False)     

    ce12_ltp=final["LTP"][(final.SYMBOL==symbolce12)].to_string(index=False)     
    ce12_iv=final["IV"][(final.SYMBOL==symbolce12)].to_string(index=False)     
    ce12_oi=final["OI"][(final.SYMBOL==symbolce12)].to_string(index=False)     
    ce12_ttv=final["TTV"][(final.SYMBOL==symbolce12)].to_string(index=False)     
    ce12_choi=final["CHNGOI"][(final.SYMBOL==symbolce12)].to_string(index=False)     

    ce13_ltp=final["LTP"][(final.SYMBOL==symbolce13)].to_string(index=False)     
    ce13_iv=final["IV"][(final.SYMBOL==symbolce13)].to_string(index=False)     
    ce13_oi=final["OI"][(final.SYMBOL==symbolce13)].to_string(index=False)     
    ce13_ttv=final["TTV"][(final.SYMBOL==symbolce13)].to_string(index=False)     
    ce13_choi=final["CHNGOI"][(final.SYMBOL==symbolce13)].to_string(index=False)     

    ce14_ltp=final["LTP"][(final.SYMBOL==symbolce14)].to_string(index=False)     
    ce14_iv=final["IV"][(final.SYMBOL==symbolce14)].to_string(index=False)     
    ce14_oi=final["OI"][(final.SYMBOL==symbolce14)].to_string(index=False)     
    ce14_ttv=final["TTV"][(final.SYMBOL==symbolce14)].to_string(index=False)     
    ce14_choi=final["CHNGOI"][(final.SYMBOL==symbolce14)].to_string(index=False)  

    ce15_ltp=final["LTP"][(final.SYMBOL==symbolce15)].to_string(index=False)     
    ce15_iv=final["IV"][(final.SYMBOL==symbolce15)].to_string(index=False)     
    ce15_oi=final["OI"][(final.SYMBOL==symbolce15)].to_string(index=False)     
    ce15_ttv=final["TTV"][(final.SYMBOL==symbolce15)].to_string(index=False)     
    ce15_choi=final["CHNGOI"][(final.SYMBOL==symbolce15)].to_string(index=False)  

    ce16_ltp=final["LTP"][(final.SYMBOL==symbolce16)].to_string(index=False)     
    ce16_iv=final["IV"][(final.SYMBOL==symbolce16)].to_string(index=False)     
    ce16_oi=final["OI"][(final.SYMBOL==symbolce16)].to_string(index=False)     
    ce16_ttv=final["TTV"][(final.SYMBOL==symbolce16)].to_string(index=False)     
    ce16_choi=final["CHNGOI"][(final.SYMBOL==symbolce16)].to_string(index=False)  

    ce17_ltp=final["LTP"][(final.SYMBOL==symbolce17)].to_string(index=False)     
    ce17_iv=final["IV"][(final.SYMBOL==symbolce17)].to_string(index=False)     
    ce17_oi=final["OI"][(final.SYMBOL==symbolce17)].to_string(index=False)     
    ce17_ttv=final["TTV"][(final.SYMBOL==symbolce17)].to_string(index=False)     
    ce17_choi=final["CHNGOI"][(final.SYMBOL==symbolce17)].to_string(index=False)  

    ce18_ltp=final["LTP"][(final.SYMBOL==symbolce18)].to_string(index=False)     
    ce18_iv=final["IV"][(final.SYMBOL==symbolce18)].to_string(index=False)     
    ce18_oi=final["OI"][(final.SYMBOL==symbolce18)].to_string(index=False)     
    ce18_ttv=final["TTV"][(final.SYMBOL==symbolce18)].to_string(index=False)     
    ce18_choi=final["CHNGOI"][(final.SYMBOL==symbolce18)].to_string(index=False)  

    ce19_ltp=final["LTP"][(final.SYMBOL==symbolce19)].to_string(index=False)     
    ce19_iv=final["IV"][(final.SYMBOL==symbolce19)].to_string(index=False)     
    ce19_oi=final["OI"][(final.SYMBOL==symbolce19)].to_string(index=False)     
    ce19_ttv=final["TTV"][(final.SYMBOL==symbolce19)].to_string(index=False)     
    ce19_choi=final["CHNGOI"][(final.SYMBOL==symbolce19)].to_string(index=False)  

    ce20_ltp=final["LTP"][(final.SYMBOL==symbolce20)].to_string(index=False)     
    ce20_iv=final["IV"][(final.SYMBOL==symbolce20)].to_string(index=False)     
    ce20_oi=final["OI"][(final.SYMBOL==symbolce20)].to_string(index=False)     
    ce20_ttv=final["TTV"][(final.SYMBOL==symbolce20)].to_string(index=False)     
    ce20_choi=final["CHNGOI"][(final.SYMBOL==symbolce20)].to_string(index=False)  

    ce21_ltp=final["LTP"][(final.SYMBOL==symbolce21)].to_string(index=False)     
    ce21_iv=final["IV"][(final.SYMBOL==symbolce21)].to_string(index=False)     
    ce21_oi=final["OI"][(final.SYMBOL==symbolce21)].to_string(index=False)     
    ce21_ttv=final["TTV"][(final.SYMBOL==symbolce21)].to_string(index=False)     
    ce21_choi=final["CHNGOI"][(final.SYMBOL==symbolce21)].to_string(index=False)  
                            
    ce22_ltp=final["LTP"][(final.SYMBOL==symbolce22)].to_string(index=False)     
    ce22_iv=final["IV"][(final.SYMBOL==symbolce22)].to_string(index=False)     
    ce22_oi=final["OI"][(final.SYMBOL==symbolce22)].to_string(index=False)     
    ce22_ttv=final["TTV"][(final.SYMBOL==symbolce22)].to_string(index=False)     
    ce22_choi=final["CHNGOI"][(final.SYMBOL==symbolce22)].to_string(index=False)  
                            
    ce23_ltp=final["LTP"][(final.SYMBOL==symbolce23)].to_string(index=False)     
    ce23_iv=final["IV"][(final.SYMBOL==symbolce23)].to_string(index=False)     
    ce23_oi=final["OI"][(final.SYMBOL==symbolce23)].to_string(index=False)     
    ce23_ttv=final["TTV"][(final.SYMBOL==symbolce23)].to_string(index=False)     
    ce23_choi=final["CHNGOI"][(final.SYMBOL==symbolce23)].to_string(index=False)  

    ce24_ltp=final["LTP"][(final.SYMBOL==symbolce24)].to_string(index=False)     
    ce24_iv=final["IV"][(final.SYMBOL==symbolce24)].to_string(index=False)     
    ce24_oi=final["OI"][(final.SYMBOL==symbolce24)].to_string(index=False)     
    ce24_ttv=final["TTV"][(final.SYMBOL==symbolce24)].to_string(index=False)     
    ce24_choi=final["CHNGOI"][(final.SYMBOL==symbolce24)].to_string(index=False)  
                            
    ce25_ltp=final["LTP"][(final.SYMBOL==symbolce25)].to_string(index=False)     
    ce25_iv=final["IV"][(final.SYMBOL==symbolce25)].to_string(index=False)     
    ce25_oi=final["OI"][(final.SYMBOL==symbolce25)].to_string(index=False)     
    ce25_ttv=final["TTV"][(final.SYMBOL==symbolce25)].to_string(index=False)     
    ce25_choi=final["CHNGOI"][(final.SYMBOL==symbolce25)].to_string(index=False)  
                            
    ce26_ltp=final["LTP"][(final.SYMBOL==symbolce26)].to_string(index=False)     
    ce26_iv=final["IV"][(final.SYMBOL==symbolce26)].to_string(index=False)     
    ce26_oi=final["OI"][(final.SYMBOL==symbolce26)].to_string(index=False)     
    ce26_ttv=final["TTV"][(final.SYMBOL==symbolce26)].to_string(index=False)     
    ce26_choi=final["CHNGOI"][(final.SYMBOL==symbolce26)].to_string(index=False)  
                            
    ce27_ltp=final["LTP"][(final.SYMBOL==symbolce27)].to_string(index=False)     
    ce27_iv=final["IV"][(final.SYMBOL==symbolce27)].to_string(index=False)     
    ce27_oi=final["OI"][(final.SYMBOL==symbolce27)].to_string(index=False)     
    ce27_ttv=final["TTV"][(final.SYMBOL==symbolce27)].to_string(index=False)     
    ce27_choi=final["CHNGOI"][(final.SYMBOL==symbolce27)].to_string(index=False)  
                            
    pe1_ltp=final["LTP"][(final.SYMBOL==symbolpe1)].to_string(index=False)     
    pe1_iv=final["IV"][(final.SYMBOL==symbolpe1)].to_string(index=False)     
    pe1_oi=final["OI"][(final.SYMBOL==symbolpe1)].to_string(index=False)     
    pe1_ttv=final["TTV"][(final.SYMBOL==symbolpe1)].to_string(index=False)     
    pe1_choi=final["CHNGOI"][(final.SYMBOL==symbolpe1)].to_string(index=False)     
    
    pe2_ltp=final["LTP"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    pe2_iv=final["IV"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    pe2_oi=final["OI"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    pe2_ttv=final["TTV"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    pe2_choi=final["CHNGOI"][(final.SYMBOL==symbolpe2)].to_string(index=False)     
    
    pe3_ltp=final["LTP"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    pe3_iv=final["IV"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    pe3_oi=final["OI"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    pe3_ttv=final["TTV"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    pe3_choi=final["CHNGOI"][(final.SYMBOL==symbolpe3)].to_string(index=False)     
    
    pe4_ltp=final["LTP"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    pe4_iv=final["IV"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    pe4_oi=final["OI"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    pe4_ttv=final["TTV"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    pe4_choi=final["CHNGOI"][(final.SYMBOL==symbolpe4)].to_string(index=False)     
    
    pe5_ltp=final["LTP"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    pe5_iv=final["IV"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    pe5_oi=final["OI"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    pe5_ttv=final["TTV"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    pe5_choi=final["CHNGOI"][(final.SYMBOL==symbolpe5)].to_string(index=False)     
    
    pe6_ltp=final["LTP"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    pe6_iv=final["IV"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    pe6_oi=final["OI"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    pe6_ttv=final["TTV"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    pe6_choi=final["CHNGOI"][(final.SYMBOL==symbolpe6)].to_string(index=False)     
    
    pe7_ltp=final["LTP"][(final.SYMBOL==symbolpe7)].to_string(index=False)     
    pe7_iv=final["IV"][(final.SYMBOL==symbolpe7)].to_string(index=False)     
    pe7_oi=final["OI"][(final.SYMBOL==symbolpe7)].to_string(index=False)     
    pe7_ttv=final["TTV"][(final.SYMBOL==symbolpe7)].to_string(index=False)     
    pe7_choi=final["CHNGOI"][(final.SYMBOL==symbolpe7)].to_string(index=False)

    pe8_ltp=final["LTP"][(final.SYMBOL==symbolpe8)].to_string(index=False)     
    pe8_iv=final["IV"][(final.SYMBOL==symbolpe8)].to_string(index=False)     
    pe8_oi=final["OI"][(final.SYMBOL==symbolpe8)].to_string(index=False)     
    pe8_ttv=final["TTV"][(final.SYMBOL==symbolpe8)].to_string(index=False)     
    pe8_choi=final["CHNGOI"][(final.SYMBOL==symbolpe8)].to_string(index=False)     

    pe9_ltp=final["LTP"][(final.SYMBOL==symbolpe9)].to_string(index=False)     
    pe9_iv=final["IV"][(final.SYMBOL==symbolpe9)].to_string(index=False)     
    pe9_oi=final["OI"][(final.SYMBOL==symbolpe9)].to_string(index=False)     
    pe9_ttv=final["TTV"][(final.SYMBOL==symbolpe9)].to_string(index=False)     
    pe9_choi=final["CHNGOI"][(final.SYMBOL==symbolpe9)].to_string(index=False)

    pe10_ltp=final["LTP"][(final.SYMBOL==symbolpe10)].to_string(index=False)     
    pe10_iv=final["IV"][(final.SYMBOL==symbolpe10)].to_string(index=False)     
    pe10_oi=final["OI"][(final.SYMBOL==symbolpe10)].to_string(index=False)     
    pe10_ttv=final["TTV"][(final.SYMBOL==symbolpe10)].to_string(index=False)     
    pe10_choi=final["CHNGOI"][(final.SYMBOL==symbolpe10)].to_string(index=False)

    pe11_ltp=final["LTP"][(final.SYMBOL==symbolpe11)].to_string(index=False)     
    pe11_iv=final["IV"][(final.SYMBOL==symbolpe11)].to_string(index=False)     
    pe11_oi=final["OI"][(final.SYMBOL==symbolpe11)].to_string(index=False)     
    pe11_ttv=final["TTV"][(final.SYMBOL==symbolpe11)].to_string(index=False)     
    pe11_choi=final["CHNGOI"][(final.SYMBOL==symbolpe11)].to_string(index=False)

    pe12_ltp=final["LTP"][(final.SYMBOL==symbolpe12)].to_string(index=False)     
    pe12_iv=final["IV"][(final.SYMBOL==symbolpe12)].to_string(index=False)     
    pe12_oi=final["OI"][(final.SYMBOL==symbolpe12)].to_string(index=False)     
    pe12_ttv=final["TTV"][(final.SYMBOL==symbolpe12)].to_string(index=False)     
    pe12_choi=final["CHNGOI"][(final.SYMBOL==symbolpe12)].to_string(index=False)

    pe13_ltp=final["LTP"][(final.SYMBOL==symbolpe13)].to_string(index=False)     
    pe13_iv=final["IV"][(final.SYMBOL==symbolpe13)].to_string(index=False)     
    pe13_oi=final["OI"][(final.SYMBOL==symbolpe13)].to_string(index=False)     
    pe13_ttv=final["TTV"][(final.SYMBOL==symbolpe13)].to_string(index=False)     
    pe13_choi=final["CHNGOI"][(final.SYMBOL==symbolpe13)].to_string(index=False)

    pe14_ltp=final["LTP"][(final.SYMBOL==symbolpe14)].to_string(index=False)     
    pe14_iv=final["IV"][(final.SYMBOL==symbolpe14)].to_string(index=False)     
    pe14_oi=final["OI"][(final.SYMBOL==symbolpe14)].to_string(index=False)     
    pe14_ttv=final["TTV"][(final.SYMBOL==symbolpe14)].to_string(index=False)     
    pe14_choi=final["CHNGOI"][(final.SYMBOL==symbolpe14)].to_string(index=False)

    pe15_ltp=final["LTP"][(final.SYMBOL==symbolpe15)].to_string(index=False)     
    pe15_iv=final["IV"][(final.SYMBOL==symbolpe15)].to_string(index=False)     
    pe15_oi=final["OI"][(final.SYMBOL==symbolpe15)].to_string(index=False)     
    pe15_ttv=final["TTV"][(final.SYMBOL==symbolpe15)].to_string(index=False)     
    pe15_choi=final["CHNGOI"][(final.SYMBOL==symbolpe15)].to_string(index=False)

    pe16_ltp=final["LTP"][(final.SYMBOL==symbolpe16)].to_string(index=False)     
    pe16_iv=final["IV"][(final.SYMBOL==symbolpe16)].to_string(index=False)     
    pe16_oi=final["OI"][(final.SYMBOL==symbolpe16)].to_string(index=False)     
    pe16_ttv=final["TTV"][(final.SYMBOL==symbolpe16)].to_string(index=False)     
    pe16_choi=final["CHNGOI"][(final.SYMBOL==symbolpe16)].to_string(index=False)

    pe17_ltp=final["LTP"][(final.SYMBOL==symbolpe17)].to_string(index=False)     
    pe17_iv=final["IV"][(final.SYMBOL==symbolpe17)].to_string(index=False)     
    pe17_oi=final["OI"][(final.SYMBOL==symbolpe17)].to_string(index=False)     
    pe17_ttv=final["TTV"][(final.SYMBOL==symbolpe17)].to_string(index=False)     
    pe17_choi=final["CHNGOI"][(final.SYMBOL==symbolpe17)].to_string(index=False)

    pe18_ltp=final["LTP"][(final.SYMBOL==symbolpe18)].to_string(index=False)     
    pe18_iv=final["IV"][(final.SYMBOL==symbolpe18)].to_string(index=False)     
    pe18_oi=final["OI"][(final.SYMBOL==symbolpe18)].to_string(index=False)     
    pe18_ttv=final["TTV"][(final.SYMBOL==symbolpe18)].to_string(index=False)     
    pe18_choi=final["CHNGOI"][(final.SYMBOL==symbolpe18)].to_string(index=False)

    pe19_ltp=final["LTP"][(final.SYMBOL==symbolpe19)].to_string(index=False)     
    pe19_iv=final["IV"][(final.SYMBOL==symbolpe19)].to_string(index=False)     
    pe19_oi=final["OI"][(final.SYMBOL==symbolpe19)].to_string(index=False)     
    pe19_ttv=final["TTV"][(final.SYMBOL==symbolpe19)].to_string(index=False)     
    pe19_choi=final["CHNGOI"][(final.SYMBOL==symbolpe19)].to_string(index=False)

    pe20_ltp=final["LTP"][(final.SYMBOL==symbolpe20)].to_string(index=False)     
    pe20_iv=final["IV"][(final.SYMBOL==symbolpe20)].to_string(index=False)     
    pe20_oi=final["OI"][(final.SYMBOL==symbolpe20)].to_string(index=False)     
    pe20_ttv=final["TTV"][(final.SYMBOL==symbolpe20)].to_string(index=False)     
    pe20_choi=final["CHNGOI"][(final.SYMBOL==symbolpe20)].to_string(index=False)

    pe21_ltp=final["LTP"][(final.SYMBOL==symbolpe21)].to_string(index=False)     
    pe21_iv=final["IV"][(final.SYMBOL==symbolpe21)].to_string(index=False)     
    pe21_oi=final["OI"][(final.SYMBOL==symbolpe21)].to_string(index=False)     
    pe21_ttv=final["TTV"][(final.SYMBOL==symbolpe21)].to_string(index=False)     
    pe21_choi=final["CHNGOI"][(final.SYMBOL==symbolpe21)].to_string(index=False)

    pe22_ltp=final["LTP"][(final.SYMBOL==symbolpe22)].to_string(index=False)     
    pe22_iv=final["IV"][(final.SYMBOL==symbolpe22)].to_string(index=False)     
    pe22_oi=final["OI"][(final.SYMBOL==symbolpe22)].to_string(index=False)     
    pe22_ttv=final["TTV"][(final.SYMBOL==symbolpe22)].to_string(index=False)     
    pe22_choi=final["CHNGOI"][(final.SYMBOL==symbolpe22)].to_string(index=False)

    pe23_ltp=final["LTP"][(final.SYMBOL==symbolpe23)].to_string(index=False)     
    pe23_iv=final["IV"][(final.SYMBOL==symbolpe23)].to_string(index=False)     
    pe23_oi=final["OI"][(final.SYMBOL==symbolpe23)].to_string(index=False)     
    pe23_ttv=final["TTV"][(final.SYMBOL==symbolpe23)].to_string(index=False)     
    pe23_choi=final["CHNGOI"][(final.SYMBOL==symbolpe23)].to_string(index=False)

    pe24_ltp=final["LTP"][(final.SYMBOL==symbolpe24)].to_string(index=False)     
    pe24_iv=final["IV"][(final.SYMBOL==symbolpe24)].to_string(index=False)     
    pe24_oi=final["OI"][(final.SYMBOL==symbolpe24)].to_string(index=False)     
    pe24_ttv=final["TTV"][(final.SYMBOL==symbolpe24)].to_string(index=False)     
    pe24_choi=final["CHNGOI"][(final.SYMBOL==symbolpe24)].to_string(index=False)

    pe25_ltp=final["LTP"][(final.SYMBOL==symbolpe25)].to_string(index=False)     
    pe25_iv=final["IV"][(final.SYMBOL==symbolpe25)].to_string(index=False)     
    pe25_oi=final["OI"][(final.SYMBOL==symbolpe25)].to_string(index=False)     
    pe25_ttv=final["TTV"][(final.SYMBOL==symbolpe25)].to_string(index=False)     
    pe25_choi=final["CHNGOI"][(final.SYMBOL==symbolpe25)].to_string(index=False)

    pe26_ltp=final["LTP"][(final.SYMBOL==symbolpe26)].to_string(index=False)     
    pe26_iv=final["IV"][(final.SYMBOL==symbolpe26)].to_string(index=False)     
    pe26_oi=final["OI"][(final.SYMBOL==symbolpe26)].to_string(index=False)     
    pe26_ttv=final["TTV"][(final.SYMBOL==symbolpe26)].to_string(index=False)     
    pe26_choi=final["CHNGOI"][(final.SYMBOL==symbolpe26)].to_string(index=False)

    pe27_ltp=final["LTP"][(final.SYMBOL==symbolpe27)].to_string(index=False)     
    pe27_iv=final["IV"][(final.SYMBOL==symbolpe27)].to_string(index=False)     
    pe27_oi=final["OI"][(final.SYMBOL==symbolpe27)].to_string(index=False)     
    pe27_ttv=final["TTV"][(final.SYMBOL==symbolpe27)].to_string(index=False)     
    pe27_choi=final["CHNGOI"][(final.SYMBOL==symbolpe27)].to_string(index=False)
         
    DIX={"TIME":current_time,"ce1_stk":[ce1_stk],"ce1_ltp":[ce1_ltp],"ce1_iv":[ce1_iv],"ce1_oi":[ce1_oi],"ce1_ttv":[ce1_ttv],"ce1_choi":[ce1_choi],
         "ce2_stk":[ce2_stk],"ce2_ltp":[ce2_ltp],"ce2_iv":[ce2_iv],"ce2_oi":[ce2_oi],"ce2_ttv":[ce2_ttv],"ce2_choi":[ce2_choi],
         "ce3_stk":[ce3_stk],"ce3_ltp":[ce3_ltp],"ce3_iv":[ce3_iv],"ce3_oi":[ce3_oi],"ce3_ttv":[ce3_ttv],"ce3_choi":[ce3_choi],
         "ce4_stk":[ce4_stk],"ce4_ltp":[ce4_ltp],"ce4_iv":[ce4_iv],"ce4_oi":[ce4_oi],"ce4_ttv":[ce4_ttv],"ce4_choi":[ce4_choi],
         "ce5_stk":[ce5_stk],"ce5_ltp":[ce5_ltp],"ce5_iv":[ce5_iv],"ce5_oi":[ce5_oi],"ce5_ttv":[ce5_ttv],"ce5_choi":[ce5_choi],
         "ce6_stk":[ce6_stk],"ce6_ltp":[ce6_ltp],"ce6_iv":[ce6_iv],"ce6_oi":[ce6_oi],"ce6_ttv":[ce6_ttv],"ce6_choi":[ce6_choi],
         "ce7_stk":[ce7_stk],"ce7_ltp":[ce7_ltp],"ce7_iv":[ce7_iv],"ce7_oi":[ce7_oi],"ce7_ttv":[ce7_ttv],"ce7_choi":[ce7_choi],
         "ce8_stk":[ce8_stk],"ce8_ltp":[ce8_ltp],"ce8_iv":[ce8_iv],"ce8_oi":[ce8_oi],"ce8_ttv":[ce8_ttv],"ce8_choi":[ce8_choi],
         "ce9_stk":[ce9_stk],"ce9_ltp":[ce9_ltp],"ce9_iv":[ce9_iv],"ce9_oi":[ce9_oi],"ce9_ttv":[ce9_ttv],"ce9_choi":[ce9_choi],
         "ce10_stk":[ce10_stk],"ce10_ltp":[ce10_ltp],"ce10_iv":[ce10_iv],"ce10_oi":[ce10_oi],"ce10_ttv":[ce10_ttv],"ce10_choi":[ce10_choi],
         "ce11_stk":[ce11_stk],"ce11_ltp":[ce11_ltp],"ce11_iv":[ce11_iv],"ce11_oi":[ce11_oi],"ce11_ttv":[ce11_ttv],"ce11_choi":[ce11_choi],
         "ce12_stk":[ce12_stk],"ce12_ltp":[ce12_ltp],"ce12_iv":[ce12_iv],"ce12_oi":[ce12_oi],"ce12_ttv":[ce12_ttv],"ce12_choi":[ce12_choi],
         "ce13_stk":[ce13_stk],"ce13_ltp":[ce13_ltp],"ce13_iv":[ce13_iv],"ce13_oi":[ce13_oi],"ce13_ttv":[ce13_ttv],"ce13_choi":[ce13_choi],
         "ce14_stk":[ce14_stk],"ce14_ltp":[ce14_ltp],"ce14_iv":[ce14_iv],"ce14_oi":[ce14_oi],"ce14_ttv":[ce14_ttv],"ce14_choi":[ce14_choi],
         "ce15_stk":[ce15_stk],"ce15_ltp":[ce15_ltp],"ce15_iv":[ce15_iv],"ce15_oi":[ce15_oi],"ce15_ttv":[ce15_ttv],"ce15_choi":[ce15_choi],
         "ce16_stk":[ce16_stk],"ce16_ltp":[ce16_ltp],"ce16_iv":[ce16_iv],"ce16_oi":[ce16_oi],"ce16_ttv":[ce16_ttv],"ce16_choi":[ce16_choi],
         "ce17_stk":[ce17_stk],"ce17_ltp":[ce17_ltp],"ce17_iv":[ce17_iv],"ce17_oi":[ce17_oi],"ce17_ttv":[ce17_ttv],"ce17_choi":[ce17_choi],
         "ce18_stk":[ce18_stk],"ce18_ltp":[ce18_ltp],"ce18_iv":[ce18_iv],"ce18_oi":[ce18_oi],"ce18_ttv":[ce18_ttv],"ce18_choi":[ce18_choi],
         "ce19_stk":[ce19_stk],"ce19_ltp":[ce19_ltp],"ce19_iv":[ce19_iv],"ce19_oi":[ce19_oi],"ce19_ttv":[ce19_ttv],"ce19_choi":[ce19_choi],
         "ce20_stk":[ce20_stk],"ce20_ltp":[ce20_ltp],"ce20_iv":[ce20_iv],"ce20_oi":[ce20_oi],"ce20_ttv":[ce20_ttv],"ce20_choi":[ce20_choi],
         "ce21_stk":[ce21_stk],"ce21_ltp":[ce21_ltp],"ce21_iv":[ce21_iv],"ce21_oi":[ce21_oi],"ce21_ttv":[ce21_ttv],"ce21_choi":[ce21_choi],
         "ce22_stk":[ce22_stk],"ce22_ltp":[ce22_ltp],"ce22_iv":[ce22_iv],"ce22_oi":[ce22_oi],"ce22_ttv":[ce22_ttv],"ce22_choi":[ce22_choi],
         "ce23_stk":[ce23_stk],"ce23_ltp":[ce23_ltp],"ce23_iv":[ce23_iv],"ce23_oi":[ce23_oi],"ce23_ttv":[ce23_ttv],"ce23_choi":[ce23_choi],
         "ce24_stk":[ce24_stk],"ce24_ltp":[ce24_ltp],"ce24_iv":[ce24_iv],"ce24_oi":[ce24_oi],"ce24_ttv":[ce24_ttv],"ce24_choi":[ce24_choi],
         "ce25_stk":[ce25_stk],"ce25_ltp":[ce25_ltp],"ce25_iv":[ce25_iv],"ce25_oi":[ce25_oi],"ce25_ttv":[ce25_ttv],"ce25_choi":[ce25_choi],
         "ce26_stk":[ce26_stk],"ce26_ltp":[ce26_ltp],"ce26_iv":[ce26_iv],"ce26_oi":[ce26_oi],"ce26_ttv":[ce26_ttv],"ce26_choi":[ce26_choi],
         "ce27_stk":[ce27_stk],"ce27_ltp":[ce27_ltp],"ce27_iv":[ce27_iv],"ce27_oi":[ce27_oi],"ce27_ttv":[ce27_ttv],"ce27_choi":[ce27_choi],

         "pe1_stk":[pe1_stk],"pe1_ltp":[pe1_ltp],"pe1_iv":[pe1_iv],"pe1_oi":[pe1_oi],"pe1_ttv":[pe1_ttv],"pe1_choi":[pe1_choi],
         "pe2_stk":[pe2_stk],"pe2_ltp":[pe2_ltp],"pe2_iv":[pe2_iv],"pe2_oi":[pe2_oi],"pe2_ttv":[pe2_ttv],"pe2_choi":[pe2_choi],
         "pe3_stk":[pe3_stk],"pe3_ltp":[pe3_ltp],"pe3_iv":[pe3_iv],"pe3_oi":[pe3_oi],"pe3_ttv":[pe3_ttv],"pe3_choi":[pe3_choi],
         "pe4_stk":[pe4_stk],"pe4_ltp":[pe4_ltp],"pe4_iv":[pe4_iv],"pe4_oi":[pe4_oi],"pe4_ttv":[pe4_ttv],"pe4_choi":[pe4_choi],
         "pe5_stk":[pe5_stk],"pe5_ltp":[pe5_ltp],"pe5_iv":[pe5_iv],"pe5_oi":[pe5_oi],"pe5_ttv":[pe5_ttv],"pe5_choi":[pe5_choi],
         "pe6_stk":[pe6_stk],"pe6_ltp":[pe6_ltp],"pe6_iv":[pe6_iv],"pe6_oi":[pe6_oi],"pe6_ttv":[pe6_ttv],"pe6_choi":[pe6_choi],
         "pe7_stk":[pe7_stk],"pe7_ltp":[pe7_ltp],"pe7_iv":[pe7_iv],"pe7_oi":[pe7_oi],"pe7_ttv":[pe7_ttv],"pe7_choi":[pe7_choi],
         "pe8_stk":[pe8_stk],"pe8_ltp":[pe8_ltp],"pe8_iv":[pe8_iv],"pe8_oi":[pe8_oi],"pe8_ttv":[pe8_ttv],"pe8_choi":[pe8_choi],
         "pe9_stk":[pe9_stk],"pe9_ltp":[pe9_ltp],"pe9_iv":[pe9_iv],"pe9_oi":[pe9_oi],"pe9_ttv":[pe9_ttv],"pe9_choi":[pe9_choi],
         "pe10_stk":[pe10_stk],"pe10_ltp":[pe10_ltp],"pe10_iv":[pe10_iv],"pe10_oi":[pe10_oi],"pe10_ttv":[pe10_ttv],"pe10_choi":[pe10_choi],
         "pe11_stk":[pe11_stk],"pe11_ltp":[pe11_ltp],"pe11_iv":[pe11_iv],"pe11_oi":[pe11_oi],"pe11_ttv":[pe11_ttv],"pe11_choi":[pe11_choi],
         "pe12_stk":[pe12_stk],"pe12_ltp":[pe12_ltp],"pe12_iv":[pe12_iv],"pe12_oi":[pe12_oi],"pe12_ttv":[pe12_ttv],"pe12_choi":[pe12_choi],
         "pe13_stk":[pe13_stk],"pe13_ltp":[pe13_ltp],"pe13_iv":[pe13_iv],"pe13_oi":[pe13_oi],"pe13_ttv":[pe13_ttv],"pe13_choi":[pe13_choi],
         "pe14_stk":[pe14_stk],"pe14_ltp":[pe14_ltp],"pe14_iv":[pe14_iv],"pe14_oi":[pe14_oi],"pe14_ttv":[pe14_ttv],"pe14_choi":[pe14_choi],
         "pe15_stk":[pe15_stk],"pe15_ltp":[pe15_ltp],"pe15_iv":[pe15_iv],"pe15_oi":[pe15_oi],"pe15_ttv":[pe15_ttv],"pe15_choi":[pe15_choi],
         "pe16_stk":[pe16_stk],"pe16_ltp":[pe16_ltp],"pe16_iv":[pe16_iv],"pe16_oi":[pe16_oi],"pe16_ttv":[pe16_ttv],"pe16_choi":[pe16_choi],
         "pe17_stk":[pe17_stk],"pe17_ltp":[pe17_ltp],"pe17_iv":[pe17_iv],"pe17_oi":[pe17_oi],"pe17_ttv":[pe17_ttv],"pe17_choi":[pe17_choi],
         "pe18_stk":[pe18_stk],"pe18_ltp":[pe18_ltp],"pe18_iv":[pe18_iv],"pe18_oi":[pe18_oi],"pe18_ttv":[pe18_ttv],"pe18_choi":[pe18_choi],
         "pe19_stk":[pe19_stk],"pe19_ltp":[pe19_ltp],"pe19_iv":[pe19_iv],"pe19_oi":[pe19_oi],"pe19_ttv":[pe19_ttv],"pe19_choi":[pe19_choi],
         "pe20_stk":[pe20_stk],"pe20_ltp":[pe20_ltp],"pe20_iv":[pe20_iv],"pe20_oi":[pe20_oi],"pe20_ttv":[pe20_ttv],"pe20_choi":[pe20_choi],
         "pe21_stk":[pe21_stk],"pe21_ltp":[pe21_ltp],"pe21_iv":[pe21_iv],"pe21_oi":[pe21_oi],"pe21_ttv":[pe21_ttv],"pe21_choi":[pe21_choi],
         "pe22_stk":[pe22_stk],"pe22_ltp":[pe22_ltp],"pe22_iv":[pe22_iv],"pe22_oi":[pe22_oi],"pe22_ttv":[pe22_ttv],"pe22_choi":[pe22_choi],
         "pe23_stk":[pe23_stk],"pe23_ltp":[pe23_ltp],"pe23_iv":[pe23_iv],"pe23_oi":[pe23_oi],"pe23_ttv":[pe23_ttv],"pe23_choi":[pe23_choi],
         "pe24_stk":[pe24_stk],"pe24_ltp":[pe24_ltp],"pe24_iv":[pe24_iv],"pe24_oi":[pe24_oi],"pe24_ttv":[pe24_ttv],"pe24_choi":[pe24_choi],
         "pe25_stk":[pe25_stk],"pe25_ltp":[pe25_ltp],"pe25_iv":[pe25_iv],"pe25_oi":[pe25_oi],"pe25_ttv":[pe25_ttv],"pe25_choi":[pe25_choi],
         "pe26_stk":[pe26_stk],"pe26_ltp":[pe26_ltp],"pe26_iv":[pe26_iv],"pe26_oi":[pe26_oi],"pe26_ttv":[pe26_ttv],"pe26_choi":[pe26_choi],
         "pe27_stk":[pe27_stk],"pe27_ltp":[pe27_ltp],"pe27_iv":[pe27_iv],"pe27_oi":[pe27_oi],"pe27_ttv":[pe27_ttv],"pe27_choi":[pe27_choi],}
         
    FINAL=pd.DataFrame(DIX)
    FINAL.to_csv("LIVE_RECORD.csv",mode="a",index=False,header=False)
    print(current_time+' '+'DATA RECORDED SUCCESSFULLY')
    time.sleep(INTERVAL*60)
for j in range(0,int(REPEAT_CODE)):
    while True:
        try:
            DATA_EXTRACT()
            break
        except:
            print("Trying to collect data")
            time.sleep(5)
        
    
        
        
        
    
   
    
    
    


    
     