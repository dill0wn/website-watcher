from urllib import request
from bs4 import BeautifulSoup  # Requires beautifulsoup4

page = request.urlopen('https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3080/').read()
soup = BeautifulSoup(page, features='html.parser')

# will always be 'ADD TO CART because JS updates. 
# need selenium or other web driver
print(soup.select('.btn-cart')[0].get_text())