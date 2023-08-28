from urllib import request
from bs4 import BeautifulSoup

# ----- 1. Read in a web page -----
## A url to read in
link = "http://www.u.arizona.edu/~hammond/"

## Use method urlopen() to create a stream to read from:
f = request.urlopen(link)
myfile = f.read() # Read the url
print(myfile)

## Use .decode() to decode the page:
print(myfile.decode('UTF-8'))

# ----- 2. Use BeautifulSoup to parse HTML -----
## See the documentation of Beautifulsoup here:
## https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# soup = BeautifulSoup(myfile,'html.parser')

## 2.1 Pretty-print html
# print(soup.prettify())

## 2.2 Get all texts:
# print(soup.get_text())

## 2.3 Get all hyperlinks:
# for link in soup.find_all('a'): # 'a': The tag <a> defines a hyperlink. See slides.
#     print(link.get('href'))

