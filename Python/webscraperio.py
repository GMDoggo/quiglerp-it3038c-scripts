import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.reebok.com/us/flexagon-energy-shoes---preschool/DV8354.html").content
soup = BeautifulSoup(data, 'html.parser')

span = soup.find("h1", {"class": "product_information_title___2rG9M product_title gl-heading gl-heading--m"})
title = re.sub(r'[^a-zA-Z0-9\s]', '', span.text)  # Remove special characters

span = soup.find("span", {"class": "gl-price__value gl-price__value--sale"})
price = re.sub(r'[^a-zA-Z0-9\s]', '', span.text)  # Remove special characters

print("Item %s has price %s" % (title, price))
