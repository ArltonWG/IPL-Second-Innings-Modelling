# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = "https://www.cricbuzz.com/cricket-series/3472/indian-premier-league-2021/matches"

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())
#print(list(soup.children))
#print([type(item) for item in list(soup.children)])
for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])
