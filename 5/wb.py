import re
import requests
urll="https://s.weibo.com/top/summary/"
headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36 Edg/117.0.2045.60"
}
cookie={"SUB":"_2AkMSRfDnf8NxqwFRmfkRyW_mb4VxzgHEieKkGQE8JRMxHRl-yT9kqmcStRB6OcXeCAxd7FXqPmQHIRtyfhpTcN1j-8D3",
        "SUBP":"0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFwEiG00sa60.1pDs3krni5",
        "_s_tentry":"link.zhihu.com",
        "Apache":"2778566363848.7466.1696768973802",
        "SINAGLOBAL":"2778566363848.7466.1696768973802",
        "ULV":"1696768973811:1:1:1:2778566363848.7466.1696768973802"}
resp=requests.get(urll,headers=headers,cookies=cookie)
resp.encoding="utf-8"
content=resp.text
pattern_top=re.compile(r'<i class="icon icon_pinned"></i>.*?<span>(.*?)</span>.*?<i class="icon icon_hot"></i>',re.S)
result_top=pattern_top.findall(content)
print(result_top)
pattern=re.compile( r'<strong class="hot">.*?<span>(.*?)<em>.*?</span>',re.S)
result=pattern.findall(content)
print(result)