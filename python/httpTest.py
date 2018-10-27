import urllib.request
import urllib.parse

data = {
    "name": "yohei",
    "age": 30,
    "comment": "あああ"
}
# POST
# ここでエンコードして文字→バイトにする
data = urllib.parse.urlencode(data).encode("utf-8")
with urllib.request.urlopen("http://www.yoheim.net/", data=data) as res:
   html = res.read().decode("utf-8")
   print(html)

""" GET
with urllib.request.urlopen("http://zipcloud.ibsnet.co.jp/api/search?zipcode=4200855") as res:
    html = res.read().decode("utf-8")
    print(html)
"""