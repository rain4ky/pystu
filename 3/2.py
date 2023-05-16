from bs4 import BeautifulSoup
import requests
import re
url="https://movie.douban.com/top250?start=50"
try:
    kv={"user-agent":'Mozilla/5.0'}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    #print(html)
    fo = open("output.html","w+",encoding="utf-8")
    fo.write(html)
    fo.close()
    print("爬取成功！")
except:
    print("爬取失败！")
soup = BeautifulSoup(html, 'lxml')
soup.prettify()
movies=soup.select('ol li')
print(movies.__class__)
for movie in movies:
    print(movie.find(name="span",class_="title").get_text())