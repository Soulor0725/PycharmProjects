from urllib import request,parse

url = 'http://httpbin.org/get'

params = {
    'name1':'value1',
    'name2':'value2',
}

queryString = parse.urlencode(params)

u = request.urlopen(url+'?'+queryString)
rep = u.read()
print(rep)


url = url = 'http://httpbin.org/post'

queryString = parse.urlencode(params)

u = request.urlopen(url, queryString.encode('ascii'))
res = u.read()
print(res)

headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}
req = request.Request(url,queryString.encode('ascii'),headers=headers)
u = request.urlopen(req)
res = u.read()
print(res)