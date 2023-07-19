import requests
from bs4 import BeautifulSoup

# send an HTTP request to the website's server and retrieve the HTML content
response = requests.get("https://www.tokopedia.com/")
html_content = response.text

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# extract the data you want using the soup object
data = soup.find("div", {"class": "example-data"}).text

# print the extracted data
print(data)