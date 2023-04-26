# coding=utf-8 
import jieba
import wordcloud
font = r'C:\Windows\Fonts\simfang.ttf'
fobj=open('C:/Users/86159/Desktop/书/倾城之恋.txt','r')
print("倾城之恋词频统计")
ftxt=fobj.read()
words=jieba.lcut(ftxt)
count={}
for word in words:
    if len(word)==1:
        continue
    else:
        count[word]=count.get(word,0)+1
items=list(count.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,num=items[i]
    print("{0:<10}{1:>5}".format(word,num))

wpng=wordcloud.WordCloud(font_path=font)
wpng.generate(ftxt)
wpng.to_file('C:/Users/86159/Desktop/cloud.png')
fobj.close()