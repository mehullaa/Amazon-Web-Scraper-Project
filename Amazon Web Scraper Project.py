#!/usr/bin/env python
# coding: utf-8

# In[13]:


#import libreries

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[44]:


URL = 'https://www.amazon.com/Crazy-Dog-T-Shirts-Birthday-Comfortab/dp/B07V5JSQ8H/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B07V5JSQ8H&psc=1&pd_rd_w=QrYSi&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=BZVN5BBCGWS24Y462Z11&pd_rd_wg=rcqJE&pd_rd_r=1a6dbb4d-8277-49ae-820b-638cc925b74d&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='desktop_unifiedPrice').get_text()

print(title)
print(price)





# In[45]:


price = price.strip()[1:]
title = title.strip()

print(title)
print(price)


# In[46]:


import datetime

today = datetime.date.today()

print(today)


# In[47]:


import csv

header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open('AmezonWebScraperDataset.csv', 'w', newline='', Tencoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

    


# In[41]:


import pandas as pd

df = pd.read_csv(r'D:\Data Analysis')

print(df)


# In[ ]:


#Now we are appending data to csv

with open ('AmezonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
        


# In[43]:


#Combine all of the above code into one function


def check_price():
    URL = 'https://www.amazon.com/Crazy-Dog-T-Shirts-Birthday-Comfortab/dp/B07V5JSQ8H/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B07V5JSQ8H&psc=1&pd_rd_w=QrYSi&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=BZVN5BBCGWS24Y462Z11&pd_rd_wg=rcqJE&pd_rd_r=1a6dbb4d-8277-49ae-820b-638cc925b74d&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='promoPriceBlockMessage_feature_div').get_text()

    price = price.strip()[1:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


# Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd

df = pd.read_csv(r'D:\Data Analysis\AmazonWebScraperDataset.csv')

print(df)


# In[48]:


# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it
# out with this script

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('mehulpanelia@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Mehul, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Crazy-Dog-T-Shirts-Birthday-Comfortab/dp/B07V5JSQ8H/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B07V5JSQ8H&psc=1&pd_rd_w=QrYSi&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=BZVN5BBCGWS24Y462Z11&pd_rd_wg=rcqJE&pd_rd_r=1a6dbb4d-8277-49ae-820b-638cc925b74d&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'mehulpanelia@gmail.com',
        msg
     
    )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




