import urllib.request
import urllib.parse
import concurrent.futures

def post():
	data = {
    "number": 1
	}
	data = urllib.parse.urlencode(data).encode("utf-8")
	with urllib.request.urlopen("http://www.yoheim.net/", data=data) as res:
	   html = res.read().decode("utf-8")
	   print(html)

def get():
	params = {
    "number": 1496
}
	p = urllib.parse.urlencode(params)
	url = "http://fullfill.sakura.ne.jp/JPHACKS2018/server.php?" + p
	print(url)

	with urllib.request.urlopen(url) as res:
		html = res.read().decode("utf-8")
		print(html)

if __name__ == "__main__":
	executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
	#executor.submit(post)
	executor.submit(get)
	print("hello")
