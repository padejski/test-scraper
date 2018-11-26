import requests
from BeautifulSoup import BeautifulSoup

url = 'https://news.google.com/search?q=%22This%20story%20was%20generated%20by%20Automated%20Insights%22&hl=en-US&gl=US&ceid=US%3Aen'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
print soup.prettify()