import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
#from selenium import webdriver
import numpy as np
#driver= webdriver.Chrome("/home/nicky/Public/chromedriver")
Stores=[]

STORE={}

data=pd.read_excel ("/home/nicky/Public/Copy of USA-Zip.xls")
#zip_codes=pd.DataFrame(data, columns=['ZIP code'])
zip_codes=data['ZIP code'].tolist()
code=np.array(zip_codes)
sorted_zip_codes=sorted(zip_codes)
codes=np.array(sorted_zip_codes)
for zip_code in codes:
    url="https://www.habitat.org/local/restore?zip=%s"%(zip_code)
    #driver.get(url)
    #content=driver.page_source
    page=requests.get(url)
    #print(zip_code)
    soup=BeautifulSoup(page.content, 'lxml')
    #results=soup.find(class_='listing')
    #print(results.prettify())
    listings = soup.find_all('article', class_='listing')
    
    for listing in listings:
        try:
            #heading=listing.find_all('div',class_='listing_body')
            heading=listing.find('h2', class_="listing__heading")
            name=heading.find('span')
            body=listing.find('div',class_="listing__body")
            address=body.find('p', class_='address')
            address_line=address.find('span', class_='address-line1')
            city=address.find('span', class_='locality')
            state=address.find('span', class_='administrative-area')
            code=address.find('span', class_='postal-code')
            items=body.find('div', class_="listing__items")
            item1=items.find('div', class_="listing__item")
            item2=item1.find_next_sibling('div', class_="listing__item")
            svg=item2.find('svg', class_="icon--small-phone icon--green")
            path=svg.find('path')
            phone=path.find_next(string=True)
            item3=item2.find_next_sibling('div', class_="listing__item")
            link=item1.find('a',href=True)
            
            STORE={
                'Name':name.text,
                'Address':address_line.text,
                'City':city.text,
                'State':state.text,
                'ZIP_Code': code.text.replace('\n',''),
                'URL': link.text.replace('\n',''),
                'Phone':phone.string.strip().replace('\n','')
            }
            if not any(d['Name']==name.text for d in Stores):
                Stores.append(STORE)
        except AttributeError:
            continue
    
    
    #print(Stores)
    csv_file='STORE1.csv'
    csv_columns=['Name', 'Address', 'City', 'State', 'ZIP_Code', 'URL','Phone']
    with open (csv_file, 'w') as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        #for data in STORE:
        writer.writerows(Stores)




