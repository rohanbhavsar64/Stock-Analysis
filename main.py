import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
from datetime import date
import streamlit as st
import time
st.title("Stock Analysis")
ticker='TATAMOTORS'
exchange='NSE'
#exchange=st.selectbox('Exchage',u)
data=pd.read_csv('Com.csv')
#st.write(data)
ticker=st.selectbox("Company",data['Symbol'].unique())
url=f'https://www.google.com/finance/quote/{ticker}:{exchange}'
df=0
from nselib import derivatives
h=0
for i in range(3):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    class1='YMlKec fxKbKc'
    price=float(soup.find(class_=class1).text.strip()[1:].replace(",",""))
    l=np.array([time.ctime()])
    df=price
    time.sleep(1)
st.subheader('Price'+':'+str(df))
st.write(h)
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
pc=soup.find(class_="P6K39c").text.strip()[1:].replace(",","")
#info=soup.find_all(id="i14")
DAYRANGE=soup.find_all('div', {'class': 'P6K39c'})[1].text
YEARRANGE=soup.find_all('div', {'class': 'P6K39c'})[2].text
MARKETCAP=soup.find_all('div', {'class': 'P6K39c'})[3].text
pe=soup.find_all('div', {'class': 'P6K39c'})[4].text
DIVIDENDYIELD=soup.find_all('div', {'class': 'P6K39c'})[5].text
PRIMARYEXCHANGE=soup.find_all('div', {'class': 'P6K39c'})[6].text
data=pd.DataFrame({"DAY RANGE":[DAYRANGE],"Previous Close":[pc],"YEAR RANGE":[YEARRANGE],"MARKET CAP":[MARKETCAP],"P/E RATIO":[pe],"DIVIDEND YIELD":[DIVIDENDYIELD],"PRIMARY EXCHANGE":[PRIMARYEXCHANGE]})
col1,col2=st.columns(2)
with col1:
    st.subheader("Stock Price V/S Time")
    i=['1D','1W','1M','1Y']
    f=st.radio('Time of Analysis',i,horizontal=True)
    df=derivatives.future_price_volume_data(ticker,'FUTSTK',period=f)
    df['Price']=df['UNDERLYING_VALUE']
    df['Date']=df['TIMESTAMP']
    df=df.drop(columns=['UNDERLYING_VALUE','TIMESTAMP'])
    import plotly.express as px
    l=px.line(df,df['Date'],df['Price'],color_discrete_sequence=["#355E3B"])
    l.update_layout(width=400,height=300,margin=dict(
       r=100,
       t=0
    ))
    st.write(l)

with col2:
    st.subheader("Stock INFO")
    d = st.table(data.transpose())
st.subheader("About")
st.write(soup.find(class_="bLLb2d").text)
Revenue=soup.find(class_="QXDnM").text
Operatingexpense=soup.find_all(class_="QXDnM")[1].text
NetIncome=soup.find_all(class_="QXDnM")[2].text
NetProfitMargin=soup.find_all(class_="QXDnM")[3].text
Earningspershare=soup.find_all(class_="QXDnM")[4].text
EBITDA=soup.find_all(class_="QXDnM")[5].text
Effectivetaxrate=soup.find_all(class_="QXDnM")[6].text
df1=pd.DataFrame({'Revenue':[Revenue],'Operating expense':[Operatingexpense],'Net Income':[NetIncome],'Net Profit Margin':[NetProfitMargin],'Earnings per share':[Earningspershare],'EBITDA':[EBITDA],"Effective tax rate":[Effectivetaxrate]})
st.subheader("Income Status")
st.table(df1.transpose())