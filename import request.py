import requests
from bs4 import BeautifulSoup
url = "https://sfbay.craigslist.org/"
# Make a GET request to the website
response = requests.get(url)
# Get the content of the response
content = response.content
# use beautifulsoup to parse the content
soup = BeautifulSoup(content,"html.parser")
# Find all the post titles
post_titles = soup.findall("a")
# print the post titles
for title in post_titles:
    print(title.text)