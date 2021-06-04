from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.amazon.in/Canon-1500D-24-1MP-Digital-55-250mm/dp/B07BRR59DT/ref=sr_1_7?dchild=1&keywords=DSLR&qid=1620822242&sr=8-7&th=1"

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
response = requests.get(URL, headers=headers)

website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

price_tag = soup.find("span", id="priceblock_ourprice")

price_name = price_tag.getText().split()[1].replace(",", "")
product_price = float(price_name)
print(product_price)
title= soup.find("span",id="productTitle").getText().strip()
print(title)
my_email = EMAIL
password = PASSWORD
if product_price > 35000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mozesachin02@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{title} is now available for {product_price} Rs"
                                f" Click on below link to purchase\n\n{URL}")
