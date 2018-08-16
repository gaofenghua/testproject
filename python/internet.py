import urllib.request

response = urllib.request.urlopen("http://helloworldbook2.com/data/message.txt")
#response = urllib.request.urlopen("http://www.baidu.com")
print(response.read())
