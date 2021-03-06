from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver= webdriver.Chrome("/home/nicky/Public/chromedriver")
products=[]
prices=[]
ratings=[]
driver.get("https://www.flipkart.com/laptops-store?otracker=nmenu_sub_Electronics_0_Laptops")

content=driver.page_source
soup=BeautifulSoup(content, "html.parser")
for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', atrrs={'class': '_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')