from bs4 import BeautifulSoup
import requests
import csv
import os
import pandas as pd
for off in range(10):
    url="https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as="+str(off)
    req=requests.get(url).text
    soup=BeautifulSoup(req,features='html5lib')
    name=soup.find_all("div",{"class":"_3wU53n"})
    price=soup.find_all("div",{"class":"_1vC4OE _2rQ-NK"})
    rating=soup.find_all("div",{"class":"hGSR34"})
    pages=soup.find("div",{"class":"_2zg3yZ"})
    print(pages.text)
    n_m=[]
    p_r=[]
    r_t=[]
    p=int(input("Enter how many data you want to fetch:"))
    for i in range(p):
                print(name[i].text)
                n_m.append(name[i].text)
                print(price[i].text)
                p_r.append(price[i].text)
                print(rating[i].text)
                r_t.append(rating[i].text)
    field=['Name','Price','Rating']
    test_result=n_m,p_r,r_t
    result=[]
    for lt in range(p):
                res=[a[lt] for a in test_result]
                result.append(res)
    filename="data"+str(off)+".csv"
    with open(filename,'w',encoding='utf-8',newline='') as writ:
                writee=csv.writer(writ)
                writee.writerow(field)
                writee.writerows(result)
                
    if(True):
                print("Data Fetched Succesfully in",filename)

