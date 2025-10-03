# url explained:  U = Uniform R = Resource L = Locator
# https://en.wikipedia.org/wiki/URL?key=value&life=42#History
# Protocol: http, https, ftp, ...
#  Host: en.wikipedia.org
#  Port: http=80, https=443
#  Path: wiki/URL
#  Querystring: key=value&life=42
#  Fragment: History


# urllib
#  request: open URLs
#  response: (used internally)
#  error: request exceptions
#  parse: useful URL functions
#  robotparser: robots.txt files

from urllib import request

resp = request.urlopen("https://www.pythoncheatsheet.org/")

#print(type(resp))

#print(resp.code)

#print(resp.length)
#print(resp.peek())

data = resp.read()
#print(type(data))

len(data)

# html = data.decode("UTF-8")
# print(type(html))
# print(html)

# HTTP Status Codes
# 200: OK
# 400: Bad Request
# 403: Forbidden
# 404: Not found

# parsing url's
# https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s

qs = "v=" + "EuC-yVzHhMI" + "&" + "t=" + "5m56s"

from urllib import parse

params = {"v": "mgkSQzj5iMM", "t": "1m56s"}
querystring = parse.urlencode(params)

print(querystring)

url = "https://www.youtube.com/watch" + "?" + querystring
print(url)
resp = request.urlopen(url)
print(resp.isclosed())
print(resp.code)

html = resp.read().decode("utf-8")
print(html[:500])