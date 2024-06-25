import plotly.graph_objects as go
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import plotly.express as px
import streamlit as st
st.title("Stock Analysis")
fd=pd.read_csv('constituents.csv')
f=fd['Symbol'].unique()
ticker=st.selectbox("Company",f)
import yfinance as yf
# Get the data for the stock AAPL
j=['Analysis','Profile','Statistics']
h=st.radio('Field',j,horizontal=True)
if h=='Analysis':
    st.subheader('Analysis')
    col1,col2=st.columns(2)
    with col1:
        l = ['5d','1wk','1mo','3mo','1y','5y','max']
        i = st.selectbox('Period', l)
        df = yf.download(ticker, period=i)
    with col2:
        q=['Area','Line','Bar']
        g=st.radio('Chart- Type',q,horizontal=True)
    if g=='Area':
        if df['Close'][-1]<df['Close'][0]:
            fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

# Display the chart using Streamlit
    st.write(fig)
    
    url3 = f'https://finance.yahoo.com/quote/{ticker}/analysis'
    r2 = requests.get(url3, headers=headers)
    w2 = BeautifulSoup(r2.text, 'html')
    f1 = w2.find_all(class_='Ta(end) Py(10px)')[0].text
    f2 = w2.find_all(class_='Ta(end) Py(10px)')[4].text
    f3 = w2.find_all(class_='Ta(end) Py(10px)')[8].text
    f4 = w2.find_all(class_='Ta(end) Py(10px)')[12].text
    f5 = w2.find_all(class_='Ta(end) Py(10px)')[16].text
    f6 = w2.find_all(class_='Ta(end) Py(10px)')[20].text
    data45 = [[f1, 'Current Qtr.'], [f2, 'Next Qtr.'], [f3, 'Current Year'], [f4, 'Next Year'],
              [f5, 'Next 5 Years (per annum)'], [f6, 'Past 5 Years (per annum)']]
    df27 = pd.DataFrame(data45, columns=['Growth Est. in %', 'Time'])
    fig27 = px.line(df27, x='Time', y='Growth Est. in %', color_discrete_sequence=['purple'],title='Growth Est. Predication')
    st.write(fig27)
elif h=='Profile':
    url1 = f'https://finance.yahoo.com/quote/{ticker}/profile'
    res = requests.get(url1, headers=headers)
    w = BeautifulSoup(res.text, 'html')
    v = w.find(class_='Mt(15px) Lh(1.6)').text
    u = w.find_all(class_='Pt(10px) smartphone_Pt(20px) Lh(1.7)')[0].text
    z = w.find_all(class_='D(ib) Va(t)')[0].text
    st.subheader('Description')
    st.write(v,fontsize=8)
else:
    st.subheader('Statistics')
    st.markdown(
        """
        <style>
            div[data-testid="column"]:nth-of-type(1)
            {
                border:1px solid white;
            } 

            div[data-testid="column"]:nth-of-type(2)
            {
                border:1px solid white;
                text-align: end;
            } 
        </style>
        """, unsafe_allow_html=True
    )
    col1,col2=st.columns(2)
    with col1:
        d1=web.find_all(class_='C($primaryColor) W(51%)')[0].text
        d2=web.find_all(class_='C($primaryColor) W(51%)')[1].text
        d3=web.find_all(class_='C($primaryColor) W(51%)')[2].text
        d4=web.find_all(class_='C($primaryColor) W(51%)')[3].text
        d5=web.find_all(class_='C($primaryColor) W(51%)')[4].text
        d6=web.find_all(class_='C($primaryColor) W(51%)')[7].text
        d7=web.find_all(class_='C($primaryColor) W(51%)')[6].text
        c1=web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[0].text
        c2=web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[1].text
        c3=web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[2].text
        c4=web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[3].text
        c5=web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[4].text
        c6=web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[5].text
        c7=web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[6].text
        d10 = web.find_all(class_='C($primaryColor) W(51%)')[7].text
        c10 = web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[7].text
        data2 = [[d1,c1], [d2,c2], [d3,c3],[d4,c4],[d5,c5],[d6,c6],[d7,c7],[d10,c10]]
        data1 = pd.DataFrame(data2,columns=['Terms','Values'])
        table=st.table(data1)
    with col2:
        d10 = web.find_all(class_='C($primaryColor) W(51%)')[7].text
        d20 = web.find_all(class_='C($primaryColor) W(51%)')[8].text
        d30= web.find_all(class_='C($primaryColor) W(51%)')[9].text
        d40= web.find_all(class_='C($primaryColor) W(51%)')[10].text
        d50= web.find_all(class_='C($primaryColor) W(51%)')[11].text
        d60= web.find_all(class_='C($primaryColor) W(51%)')[12].text
        d70= web.find_all(class_='C($primaryColor) W(51%)')[13].text
        c10= web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[7].text
        c20= web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[8].text
        c30= web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[9].text
        c40= web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[10].text
        c50= web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[11].text
        c60= web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[12].text
        c70= web.find_all(class_="Ta(end) Fw(600) Lh(14px)")[13].text
        data20 = [[d20, c20], [d30, c30], [d40, c40], [d50, c50], [d60, c60], [d70, c70]]
        data10 = pd.DataFrame(data20, columns=['Terms', 'Values'])
        table = st.table(data10)
    url2 = f'https://finance.yahoo.com/quote/{ticker}/financials'
    r1 = requests.get(url2, headers=headers)
    w1 = BeautifulSoup(r1.text, 'html')
    tr = w1.find_all(
        class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')[0].text
    tr2023 = w1.find_all(
        class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')[
        1].text
    tr2022 = w1.find_all(
        class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')[
        2].text
    tr2021 = w1.find_all(
        class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')[
        3].text
    tr2020 = w1.find_all(
        class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')[
        4].text
    inc = w1.find_all(
        class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')[
        71].text
    inc23 = w1.find_all(
        class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')[
        72].text
    inc22 = w1.find_all(
        class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')[
        73].text
    inc21 = w1.find_all(
        class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')[
        74].text
    inc20 = w1.find_all(
        class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')[
        75].text
    y1=w1.find_all(class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b)')[0].text
    y2=w1.find_all(class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b) Bgc($lv1BgColor)')[0].text
    y3=w1.find_all(class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b)')[1].text
    y4=w1.find_all(class_='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b) Bgc($lv1BgColor)')[1].text
    data5 = [[tr2023, inc23,y1], [tr2022, inc22, y2], [tr2021, inc21, y3], [tr2020, inc20, y4]]
    df21 = pd.DataFrame(data5, columns=['Total Revanue', 'income', 'Year'])
    df21['Total Revanue'] = df21['Total Revanue'].str.replace(',', '').astype(float)
    df21['income'] = df21['income'].str.replace(',', '').astype(int)
    fig21 = px.bar(df21, x='Year', y=['Total Revanue', 'income'], barmode=None,
                   title='Revanue and Income Status Per Year',color_discrete_sequence=['blue','yellow'])
    st.write(fig21)
    url3 = f'https://finance.yahoo.com/quote/{ticker}/analysis'
    r2 = requests.get(url3, headers=headers)
    w2 = BeautifulSoup(r2.text, 'html')
    a1 = w2.find_all(class_='Fw(400) W(20%) Fz(xs) C($tertiaryColor) Ta(end)')[8].text
    a2 = w2.find_all(class_='Fw(400) W(20%) Fz(xs) C($tertiaryColor) Ta(end)')[9].text
    a3 = w2.find_all(class_='Fw(400) W(20%) Fz(xs) C($tertiaryColor) Ta(end)')[10].text
    a4 = w2.find_all(class_='Fw(400) W(20%) Fz(xs) C($tertiaryColor) Ta(end)')[11].text
    b1 = w2.find_all(class_='Ta(end)')[56].text
    b2 = w2.find_all(class_='Ta(end)')[57].text
    b3 = w2.find_all(class_='Ta(end)')[58].text
    b4 = w2.find_all(class_='Ta(end)')[59].text
    c1 = w2.find_all(class_='Ta(end)')[60].text
    c2 = w2.find_all(class_='Ta(end)')[61].text
    c3 = w2.find_all(class_='Ta(end)')[62].text
    c4 = w2.find_all(class_='Ta(end)')[63].text
    data = [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3], [a4, b4, c4]]
    df17 = pd.DataFrame(data, columns=['history', 'Est.', 'Actual'])
    fig17 = px.scatter(df17, x='history', y=['Est.', 'Actual'], title='Consensus EPS',color_discrete_sequence=['grey','green'])
    fig17.update_traces(marker=dict(size=20,
                                    line=dict(width=2,
                                              color='rgba(135, 206, 250, 0.5)')),
                        selector=dict(mode='markers'))
    st.write(fig17)

#<div class="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)" data-test="left-summary-table"><table class="W(100%)"><tbody><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Previous Close</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="PREV_CLOSE-value">107.87</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Open</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="OPEN-value">107.60</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Bid</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="BID-value">0.00 x 900</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Ask</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="ASK-value">106.08 x 800</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Day's Range</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="DAYS_RANGE-value">106.75 - 108.12</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>52 Week Range</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="FIFTY_TWO_WK_RANGE-value">85.35 - 113.14</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Volume</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="TD_VOLUME-value"><fin-streamer data-symbol="MMM" data-field="regularMarketVolume" data-trend="none" data-pricehint="2" data-dfield="longFmt" value="4,449,245" active="">4,449,245</fin-streamer></td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) Bdbw(0)! "><td class="C($primaryColor) W(51%)"><span>Avg. Volume</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="AVERAGE_VOLUME_3MONTH-value">4,952,249</td></tr></tbody></table></div>
##72C73C
#l-align: inherit;">-0.55</font></font></span></fin-streamer> <fin-streamer class="Fw(500) Pstart(8px) Fz(24px)" data-symbol="INFY" data-field="regularMarketChangePercent" data-trend="txt" data-pricehint="2" data-template="({fmt})" value="-0.03539356" active=""><span class="e3b14781 ee3e99dd f5a023e1"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">(-2.88%)</font></font></span></fin-streamer><fin-streamer class="D(n)" data-symbol="INFY" changeev="regularTimeChange" data-field="regularMarketTime" data-trend="none" value="" active="true"></fin-streamer><fin-streamer class="D(n)" data-symbol="INFY" changeev="marketState" data-field="marketState" data-trend="none" value="" active="true"></fin-streamer><div id="quote-market-notice" class="C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm Whs(n)"><span>As of  09:41AM EDT. Market open.</span></div></div></div><div class="Pos(r) Z(1) D(ib) Mstart(30px) Va(t) uba-container"><div id="defaultTRADENOW-sizer" class="Ta(c) Pos-r Z-0 Pos(r) Z(a) sdaLite_D(n)" data-google-query-id="CLmUxPS9hYUDFUWjrAIdTtgCYw" style="display: none;"><div id="defaultTRADENOW-wrapper" class=""><div id="defaultdestTRADENOW" class="" style="height:55px;width:280px;"> </div></div></div></div></div>
