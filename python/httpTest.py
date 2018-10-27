import urllib.request
import urllib.parse
import concurrent.futures

def post():
	data = {
    "name": "yohei",
    "age": 30,
    "comment": "あああ"
	}
	data = urllib.parse.urlencode(data).encode("utf-8")
	with urllib.request.urlopen("http://www.yoheim.net/", data=data) as res:
	   html = res.read().decode("utf-8")
	   print(html)

def get():
	with urllib.request.urlopen("http://zipcloud.ibsnet.co.jp/api/search?zipcode=4200855") as res:
		html = res.read().decode("utf-8")
		print(html)

if __name__ == "__main__":
	executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
	executor.submit(post)
	executor.submit(get)
	print("hello")
