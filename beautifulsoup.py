from bs4 import BeautifulSoup
import urllib.request, urllib.parse,urllib.error
url = input("enter URL of website you want to scrape")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('a')
count = 0
for tag in tags:
    print(tag.get('href',None))
    count+=1
print("there are ",count," https://saif-ur-rehman19.github.io/my-page/")