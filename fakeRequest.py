import requests

url = 'http://www.sqlzoo.net'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
count =0
while(count <9):
	response = requests.get(url, headers=headers)
	print(response.content)
	count = count +1
print "Done Request"
