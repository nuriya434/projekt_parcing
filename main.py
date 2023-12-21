import requests
from bs4 import BeautifulSoup
import datetime

url="https://www.binance.com/en-KZ"

responce=requests.get(url)
soup = BeautifulSoup(responce.text, 'lxml')

names = soup.find_all("div", class_="css-1ev4kiq")
prices=soup.find_all("div", class_="coinRow-coinPrice css-1ld3mhe")
tenge_currency=5

with open ("kripta.txt", 'w', encoding='utf-8') as f:
    f.write(f"Today's {datetime.datetime.now()}")
    f.write("\n\nCoins in BINANCE in ₽:\n")

for i in range(len(names)):
    with open ("kripta.txt", 'a', encoding='utf-8') as f:
        x=f"{names[i].text} {prices[i].text[1:]} ₽\n"
        f.write(x)
with open ("kripta.txt", 'a', encoding='utf-8') as f:
    f.write("\nCoins in BINANCE in ₸:\n₸=5\n")

for i in range(len(names)):
    izn=prices[i].text[1:]
    sp=izn.split(",")
    if len(sp)==2:
        price=float(sp[0]+sp[1])*5
    else:
        price=float(sp[0])*5

    with open ("kripta.txt", 'a', encoding='utf-8') as f:
        x=f"{names[i].text} {price} ₸\n"
        f.write(x)


