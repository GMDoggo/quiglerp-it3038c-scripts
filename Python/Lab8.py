import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.scrapethissite.com/pages/simple/").content
soup = BeautifulSoup(data, 'html.parser')

#Find Div elements
country_divs = soup.find_all("div", {"class": "col-md-4 country"})

span = soup.find("h3", {"class": "country-name"})  
Country = span.text 
span = soup.find("span", {"class": "country-capital"}) 
capital = span.text 
#Had to trim the leading and trailing whitepace from extracted text.
print(f"Country {Country.strip()} has a capital of {capital.strip()}")




