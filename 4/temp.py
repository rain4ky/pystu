# coding=UTF-8
import re
import requests
urls=[]
titles=[]
dates=[]
urll="https://www.zjcs.net.cn/xinwenwang/zhxw.htm"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"
    }
resp=requests.get(urll,headers=headers)
resp.encoding="utf-8"
content=resp.text
pattern=re.compile( r'<dd id="line_u10_.?">.*?<a href="(.*?)" class="fl">(.*?)</a>.*?<span class="fr gray">(.*?)</span>.*?</dd>',re.S)
result=pattern.findall(content)
end=re.findall(r'<a href="zhxw/1.htm">(.*?)</a></span>',content)
ed=int(end[0])
for i in range(0,len(result)):
    urls.append("https://www.zjcs.net.cn/xinwenwang/"+result[i][0])
    titles.append(result[i][1])
    dates.append(result[i][2])
for i in range(ed,690,-1):
    #虽然只是到690，但是可以改成1，爬取全部数据
    urll="https://www.zjcs.net.cn/xinwenwang/zhxw/{}.htm".format(i)
    resp=requests.get(urll,headers=headers)
    resp.encoding="utf-8"
    content=resp.text
    pattern=re.compile( r'<dd id="line_u10_.?".*?>.*?<a href="../(.*?)" class="fl">(.*?)</a>.*?<span class="fr gray">(.*?)</span>.*?</dd>',re.S)
    result=pattern.findall(content)
    for i in range(0,len(result)):
        urls.append("https://www.zjcs.net.cn/xinwenwang/"+result[i][0])
        titles.append(result[i][1])
        dates.append(result[i][2])
for i in range(0,len(urls)):
    #这里只输出了新闻网页的url，但是修改输出都挺方便的
    print(urls[i])