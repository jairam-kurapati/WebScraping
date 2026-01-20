import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name = []
Price_list = [] 
Description = []
Reviews = []

for i in range(2,12):
 url = "https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"+str(i)

 r = requests.get(url)
 print(r)


 soup = BeautifulSoup(r.text, "lxml")
 box = soup.find("div",class_ = "QSCKDh dLgFEE")

 names = box.find_all("div",class_= "RG5Slk")

 for i in names:
    name = i.text
    Product_name.append(name)
    
 print(Product_name)

 price_tags = box.find_all("div", class_="hZ3P6w DeU9vF")

 for i in price_tags:
    Price_list.append(i.text.strip())

 print(Price_list)

 desc = box.find_all("ul",class_ = "HwRTzP")

 for i in desc:
    name= i.text
    Description.append(name)
    
 print(Description)

 reviews = box.find_all("div",class_ = "MKiFS6")

 for i in reviews:
    name = i.text
    Reviews.append(name)
    
 print(Reviews)
 
df = pd.DataFrame({"Product Name":Product_name,"Prices":Price_list,"Description":Description,"Reviews":Reviews})
print(df)

df.to_csv("C:/Users/jayar/OneDrive/Desktop/flipkart_mobiles_under_50000.csv")
 
 
 
 
 
 
#print(soup)
#while True:
 #np = soup.find("a",class_="jgg0SZ").get("href")
 #cnp = "https://www.flipkart.com"+np
 #print(cnp)

 #url = cnp
 #r = requests.get(url)
 #soup = BeautifulSoup(r.text,"lxml")
 
            