import requests
from bs4 import BeautifulSoup
import smtplib
def check_price():
    URL="https://www.amazon.in/Anti-Theft-Daring-Texture-Laptop-Backpack/dp/B01N5K59SU"

    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

    page=requests.get(URL,headers=header)

    soup1=BeautifulSoup(page.content,"html.parser")
    soup2=BeautifulSoup(soup1.prettify(),"html.parser")

    title=soup2.find(id='productTitle').getText()
    price=soup2.find(id='priceblock_ourprice').getText()
    cprice=price[15:20]
    cprice=cprice.replace(",",".")
    cprice=float(cprice)

    if cprice >2.0:
        send_mail()
    else:
        print("Its still the same")

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('nishanth2prem8@gmail.com','oflxfwozjpnioekn')

    subject="Price Fell Down!"
    body='Check Amazon Link : https://www.amazon.in/Anti-Theft-Daring-Texture-Laptop-Backpack/dp/B01N5K59SU'

    msg=f"Subject:{subject}\n\n {body}"

    server.sendmail(
        "nishanth2prem8@gmail.com",
        "nishanthprem8@gmail.com",
        msg

    )

    print ("Email has been sent")
    server.quit()
check_price()