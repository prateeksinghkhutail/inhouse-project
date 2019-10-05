from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}


app = Flask(__name__)


@app.route('/')
def homepage_script():
    return render_template("homepage.html")


@app.route('/about')
def about_script():
    return render_template("about.html")


@app.route('/login')
def login_script():
    return render_template("login.html")


@app.route('/mobiles')
def mobiles_script():
    return render_template("mobiles.html")


@app.route('/laptops')
def laptops_script():
    return render_template("laptops.html")


@app.route('/tv')
def tv_script():
    return render_template("tv.html")







#app route for tvs company list
@app.route('/tvcompany/<variable7>')
def tvlist_script(variable7):
    
    if variable7== "samsung":
        url8="https://www.mysmartprice.com/electronics/pricelist/samsung-tv-price-list-in-india.html"
    elif variable7== "sony":
        url8="https://www.mysmartprice.com/electronics/pricelist/sony-tv-price-list-in-india.html"
    elif variable7== "lg":
        url8="https://www.mysmartprice.com/electronics/pricelist/lg-tv-price-list-in-india.html"
    else:
        url8="https://www.mysmartprice.com/electronics/pricelist/toshiba-tv-price-list-in-india.html"

    product_images_tv=[]
    product_images_tv2=[]
    product_names_tv=[]
    tvspecs=[]
    product_link_tv=[]
    
    page=requests.get(url8)
    content = page.content
    soup=BeautifulSoup(content,"html.parser")

    name=soup.find('h1',attrs={'class':'list-info__ttl js-list-ttl'})
    company_name_tv=name.text
    
    for images in soup.find_all('img', attrs={'class':'prdct-item__img'}):
        product_images_tv.append(images.get('src'))

    for images in soup.find_all('img', attrs={'class':'prdct-item__img'}):
        product_images_tv2.append(images.get('data-lazy-src'))
    
    for product in soup.findAll('a', attrs={'class':'prdct-item__name'}):
        product_names_tv.append(product.text)
    
    for productspecs in soup.findAll('div', attrs={'class':'prdct-item__spcftn-wrpr'}):
        tvspecs.append(productspecs.text)
    
    for info in soup.findAll('div', attrs={'class':'list-info__dscrptn'}):
       productinfo_tv=info.text

    tags = soup.find_all('a',attrs={'class':'prdct-item__name'})
    for tag in tags:
        tag=tag.get('href')
        tag=tag.split("w.")[1]
        tag=tag.split("/")[2]
        product_link_tv.append(tag)

    return render_template("tvcompany.html",tvspecs=tvspecs,product_link_tv=product_link_tv,variable7=variable7,company_name_tv=company_name_tv,productinfo_tv=productinfo_tv,product_images_tv=product_images_tv,product_images_tv2=product_images_tv2,product_names_tv=product_names_tv)




#app route for comaprison of prices of tvs
@app.route('/tvcompany/<variable8>/<variable9>')
def tvlistcompare_script(variable8,variable9):
    
    if variable8== "samsung":
        url8="https://www.mysmartprice.com/electronics/pricelist/samsung-tv-price-list-in-india.html"
    elif variable8== "sony":
        url8="https://www.mysmartprice.com/electronics/pricelist/sony-tv-price-list-in-india.html"
    elif variable8== "lg":
        url8="https://www.mysmartprice.com/electronics/pricelist/lg-tv-price-list-in-india.html"
    elif variable8== "toshiba":
        url8="https://www.mysmartprice.com/electronics/pricelist/toshiba-tv-price-list-in-india.html"

    tvproducts=[] 
    tvprices=[] 
    product_link_tv2=[]
    companylogo=[]
    product_link_tv3=[]
    product_images_compare=[]
    
    page=requests.get(url8)
    content = page.content
    soup=BeautifulSoup(content,"html.parser")

    tvtags = soup.find_all('a',attrs={'class':'prdct-item__name'})
    for tvtag in tvtags:
        tvtag=tvtag.get('href')
        product_link_tv2.append(tvtag)
        tvtag=tvtag.split("w.")[1]
        tvtag=tvtag.split("/")[2]
        product_link_tv3.append(tvtag)
    for i in range(0,len(tvtags)):
        if product_link_tv3[i]==variable9:
            url9=product_link_tv2[i]

    page=requests.get(url9)
    content = page.content
    soup=BeautifulSoup(content,"html.parser")

   
    
    for price in soup.findAll('div',attrs={'class':'prc-tbl__prc'}):
        tvprices.append(price.text)
   
    for details in soup.findAll('h1',attrs={'class':'prdct-dtl__ttl'}):
        tvprodetails=(details.text)
    j=0
    for logo in soup.findAll('img',attrs={'class' : 'prdct-dtl__str-icon'}):
        companylogo.append(logo.get('src'))
        j=j+1
    for images in soup.find_all('img', attrs={'class':'prdct-dtl__img'}):
        product_images_compare.append(images.get('data-lazy-src'))

  
 
    return render_template("tvcompare.html",j=j,companylogo=companylogo,tvprodetails=tvprodetails,tvprices=tvprices,product_images_compare=product_images_compare)
    



#app route for laptops comapany list
@app.route('/laptopscompany/<variable4>')
def laptopslist_script(variable4):
    
    if variable4== "dell":
        url5="https://www.mysmartprice.com/computer/pricelist/dell-laptop-price-list-in-india.html"
    elif variable4== "hp":
        url5="https://www.mysmartprice.com/computer/pricelist/hp-laptop-price-list-in-india.html"
    elif variable4== "lenovo":
        url5="https://www.mysmartprice.com/computer/pricelist/lenovo-laptop-price-list-in-india.html"
    else:
        url5="https://www.mysmartprice.com/computer/pricelist/laptops-price-list-in-india.html"


    page=requests.get(url5)
    content = page.content
    soup=BeautifulSoup(content,"html.parser")
    
    product_images_laptop=[]
    product_images_laptop2=[]
    product_names_laptop=[]
    product_link_laptop=[]
    pspecs=[]
    
    name=soup.find('h1',attrs={'class':'list-info__ttl js-list-ttl'})
    company_name_laptop=name.text
    
    for images in soup.find_all('img', attrs={'class':'prdct-item__img'}):
        product_images_laptop.append(images.get('src'))

    for images in soup.find_all('img', attrs={'class':'prdct-item__img'}):
        product_images_laptop2.append(images.get('data-lazy-src'))
    
    for product in soup.findAll('a', attrs={'class':'prdct-item__name'}):
        product_names_laptop.append(product.text)
    
    for productspecs in soup.findAll('div', attrs={'class':'prdct-item__spcftn-wrpr'}):
        pspecs.append(productspecs.text)
    
    for info in soup.findAll('div', attrs={'class':'list-info__dscrptn'}):
       productinfo_laptop=info.text
    
    tags = soup.find_all('a',attrs={'class':'prdct-item__name'})
    for tag in tags:
        tag=tag.get('href')
        tag=tag.split("w.")[1]
        tag=tag.split("/")[2]
        product_link_laptop.append(tag)
    
    return render_template("laptopscompany.html",pspecs=pspecs,product_link_laptop=product_link_laptop,variable4=variable4,company_name_laptop=company_name_laptop,productinfo_laptop=productinfo_laptop,product_images_laptop2=product_images_laptop2,product_images_laptop=product_images_laptop,product_names_laptop=product_names_laptop)
   



#app route for comaprison of prices of laptops
@app.route('/laptopscompany/<variable5>/<variable6>')
def laptopslistcompare_script(variable5,variable6):
    
    laptopproducts=[] 
    laptopprices=[] 
    product_link_laptop2=[]
    product_link_laptop3=[]
    product_images_compare=[]
    companylogo=[]

    if variable5== "dell":
        url6="https://www.mysmartprice.com/computer/pricelist/dell-laptop-price-list-in-india.html"
    elif variable5== "hp":
        url6="https://www.mysmartprice.com/computer/pricelist/hp-laptop-price-list-in-india.html"
    elif variable5=="lenovo":
        url6="https://www.mysmartprice.com/computer/pricelist/lenovo-laptop-price-list-in-india.html"
    else:
        url6="https://www.mysmartprice.com/computer/pricelist/laptops-price-list-in-india.html"

    page=requests.get(url6)
    content = page.content
    soup=BeautifulSoup(content,"html.parser")
    
    laptoptags = soup.find_all('a',attrs={'class':'prdct-item__name'})
    for laptoptag in laptoptags:
        laptoptag=laptoptag.get('href')
        product_link_laptop2.append(laptoptag)
        laptoptag=laptoptag.split("w.")[1]
        laptoptag=laptoptag.split("/")[2]
        product_link_laptop3.append(laptoptag)
    for i in range(0,len(laptoptags)):
        if product_link_laptop3[i]==variable6:
            url6=product_link_laptop2[i]
    
    page=requests.get(url6)
    content = page.content
    soup=BeautifulSoup(content,"html.parser")
    
    for details in soup.findAll('h1', attrs={'class':'prdct-dtl__ttl'}):
        laptopprodetails=(details.text)
    
    for price in soup.findAll('div',attrs={'class':'prc-tbl__prc'}):
        laptopprices.append(price.text)
    j=0
    for logo in soup.findAll('img',attrs={'class' : 'prdct-dtl__str-icon'}):
        companylogo.append(logo.get('src'))
        j=j+1
 
    for images in soup.find_all('img', attrs={'class':'prdct-dtl__img'}):
        product_images_compare.append(images.get('data-lazy-src'))


 
    return render_template("laptopcompare.html",j=j,companylogo=companylogo,laptopprodetails=laptopprodetails,laptopprices=laptopprices,product_images_compare=product_images_compare)
    



#app route for mobiles comapany list
@app.route('/mobilescompany/<variable1>')
def mobileslist_script(variable1):
    
    if variable1== "xiaomi":
        url2="https://www.mysmartprice.com/mobile/pricelist/xiaomi-mobile-price-list-in-india.html"
    elif variable1== "samsung":
        url2="https://www.mysmartprice.com/mobile/pricelist/samsung-mobile-price-list-in-india.html"
    elif variable1== "vivo":
        url2="https://www.mysmartprice.com/mobile/pricelist/vivo-mobile-price-list-in-india.html"
    elif variable1== "oppo":
        url2="https://www.mysmartprice.com/mobile/pricelist/oppo-mobile-price-list-in-india.html"
    elif variable1== "lenovo":
        url2="https://www.mysmartprice.com/mobile/pricelist/lenovo-mobile-price-list-in-india.html"
    elif variable1== "apple":
        url2="https://www.mysmartprice.com/mobile/pricelist/apple-mobile-price-list-in-india.html"
    elif variable1== "moto":
        url2="https://www.mysmartprice.com/mobile/pricelist/motorola-mobile-price-list-in-india.html"
    elif variable1== "nokia":
        url2="https://www.mysmartprice.com/mobile/pricelist/nokia-mobile-price-list-in-india.html"
    elif variable1== "huawei":
        url2="https://www.mysmartprice.com/mobile/pricelist/huawei-mobile-price-list-in-india.html"
    elif variable1=="asus":
        url2="https://www.mysmartprice.com/mobile/pricelist/asus-mobile-price-list-in-india.html"
    else:
        url2="https://www.mysmartprice.com/mobile/pricelist/latest-mobile-phones.html"
    page=requests.get(url2)
    content = page.content
    soup=BeautifulSoup(content,"html.parser")
    
    product_images=[]
    product_names=[]
    product_images2=[]
    product_specs1=[]
    product_specs2=[]
    product_specs3=[]
    product_specs4=[]
    product_specs5=[]
    product_specs6=[]
    product_specs7=[]
    product_specs8=[]
    product_link=[]
    
    name=soup.find('h1',attrs={'class':'list-info__ttl js-list-ttl'})
    company_name=name.text

    tags = soup.find_all('a',attrs={'class':'prdct-item__name'})
    for tag in tags:
        tag=tag.get('href')
        tag=tag.split("w.")[1]
        tag=tag.split("/")[2]
        product_link.append(tag)
    for images in soup.find_all('img', attrs={'class':'prdct-item__img'}):
        product_images.append(images.get('src'))

    for images in soup.find_all('img', attrs={'class':'prdct-item__img'}):
        product_images2.append(images.get('data-lazy-src'))
    
    for product in soup.findAll('a', attrs={'class':'prdct-item__name'}):
       product_names.append(product.text)

    for productspecs in soup.findAll('li', attrs={'class':'prdct-item__spcftn kyspc__item--cpu'}):
       product_specs1.append(productspecs.text)

    for productspecs in soup.findAll('li', attrs={'class':'prdct-item__spcftn kyspc__item--ram'}):
       product_specs2.append(productspecs.text)

    for productspecs in soup.findAll('li', attrs={'class':'prdct-item__spcftn kyspc__item--strge'}):
       product_specs3.append(productspecs.text)

    for productspecs in soup.findAll('li', attrs={'class':'prdct-item__spcftn kyspc__item--bttry'}):
       product_specs4.append(productspecs.text)

    for productspecs in soup.findAll('li', attrs={'class':'prdct-item__spcftn kyspc__item--cmra'}):
       product_specs5.append(productspecs.text)

    for productspecs in soup.findAll('li', attrs={'class':'prdct-item__spcftn kyspc__item--aspct'}):
       product_specs6.append(productspecs.text)

    for productspecs in soup.findAll('li', attrs={'class':'prdct-item__spcftn kyspc__item--sim'}):
       product_specs7.append(productspecs.text)

    for productspecs in soup.findAll('li', attrs={'class':'prdct-item__spcftn kyspc__item--os'}):
       product_specs8.append(productspecs.text)
    
    for info in soup.findAll('div', attrs={'class':'list-info__dscrptn'}):
       productinfo=info.text
    
    return render_template("mobilecompany.html",variable1=variable1,product_link=product_link,company_name=company_name,productinfo=productinfo,product_images2=product_images2,product_images=product_images,product_names=product_names,product_specs1=product_specs1,product_specs2=product_specs2,product_specs3=product_specs3,product_specs4=product_specs4,product_specs5=product_specs5,product_specs6=product_specs6,product_specs7=product_specs7,product_specs8=product_specs8)
    



#app route for comaprison of prices of mobiles
@app.route('/<variable3>/<variable2>')
def mobileslistcompare_script(variable3,variable2):
    
    mobileproducts=[] 
    mobileprices=[] 
    companylogo=[]
    product_link2=[]
    product_link3=[]
    product_images_compare=[]

    if variable3== "xiaomi":
        url4="https://www.mysmartprice.com/mobile/pricelist/xiaomi-mobile-price-list-in-india.html"
    elif variable3== "samsung":
        url4="https://www.mysmartprice.com/mobile/pricelist/samsung-mobile-price-list-in-india.html"
    elif variable3== "vivo":
        url4="https://www.mysmartprice.com/mobile/pricelist/vivo-mobile-price-list-in-india.html"
    elif variable3== "oppo":
        url4="https://www.mysmartprice.com/mobile/pricelist/oppo-mobile-price-list-in-india.html"
    elif variable3== "lenovo":
        url4="https://www.mysmartprice.com/mobile/pricelist/lenovo-mobile-price-list-in-india.html"
    elif variable3== "apple":
        url4="https://www.mysmartprice.com/mobile/pricelist/apple-mobile-price-list-in-india.html"
    elif variable3== "moto":
        url4="https://www.mysmartprice.com/mobile/pricelist/motorola-mobile-price-list-in-india.html"
    elif variable3== "nokia":
        url4="https://www.mysmartprice.com/mobile/pricelist/nokia-mobile-price-list-in-india.html"
    elif variable3== "huawei":
        url4="https://www.mysmartprice.com/mobile/pricelist/huawei-mobile-price-list-in-india.html"
    elif variable3=="asus":
        url4="https://www.mysmartprice.com/mobile/pricelist/asus-mobile-price-list-in-india.html"
    else:
        url4="https://www.mysmartprice.com/mobile/pricelist/latest-mobile-phones.html"
    page=requests.get(url4)
    content = page.content
    soup=BeautifulSoup(content,"html.parser")
    
    tags = soup.find_all('a',attrs={'class':'prdct-item__name'})
    for tag in tags:
        tag=tag.get('href')
        product_link2.append(tag)
        tag=tag.split("w.")[1]
        tag=tag.split("/")[2]
        product_link3.append(tag)   

    for i in range(0,len(tags)):
        if product_link3[i]==variable2:
            url3=product_link2[i]
    
    page=requests.get(url3)
    content = page.content
    soup=BeautifulSoup(content,"html.parser")
    for details in soup.findAll('h1', attrs={'class':'prdct-dtl__ttl'}):
        mobileprodetails=(details.text)
    
    for price in soup.findAll('div',attrs={'class':'prc-tbl__prc'}):
        mobileprices.append(price.text)
    
    

    for images in soup.find_all('img', attrs={'class':'prdct-dtl__img'}):
        product_images_compare.append(images.get('data-lazy-src'))
    j=0
    for logo in soup.findAll('img',attrs={'class' : 'prdct-dtl__str-icon'}):
        companylogo.append(logo.get('src'))
        j=j+1
    for price in soup.findAll('div',attrs={'class':'prc-tbl__prc'}):
        mobileprices.append(price.text)

    
 
   
    return render_template("mobilecompare.html",j=j,companylogo=companylogo,mobileprodetails=mobileprodetails,mobileprices=mobileprices,product_images_compare=product_images_compare)
    




if __name__ == "__main__":
    app.run(debug=True)


