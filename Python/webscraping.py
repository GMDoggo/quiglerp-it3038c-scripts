from bs4 import BeautifulSoup
import requests
import re
import string 


def remove_non_printable(text):
    return ''.join(filter(lambda x: x in string.printable, text))

r = requests.get('https://analytics.usa.gov').content
soup = BeautifulSoup(r, "lxml")

print(type(soup))
print(remove_non_printable(soup.prettify()[:100]))

for link in soup.find_all('a', attrs={'href':re.compile("^https://github.com")}): 
    print(link) 
