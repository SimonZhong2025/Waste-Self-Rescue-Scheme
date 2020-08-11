### 爬取网页的通用代码框架
```
try:
    r = requests.get(url, timeout = 50)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
except:
    return "产生异常"
```

```
import requests
url = "http://sdfvsdfsfs"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encodingg
    print(r.text[1000:2000]) # 有何分别？
except:
    print("失败")
```
