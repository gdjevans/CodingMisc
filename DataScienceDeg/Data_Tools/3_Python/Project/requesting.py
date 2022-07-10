import requests

r = requests.get('https://postman-echo.com/get?foo1=bar1&foo2=bar2')
print(r.content)