import requests
from bs4 import BeautifulSoup

requests.head = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
response = requests.get('https://www.zhihu.com/')


print(response.status_code)

# &quot;title&quot;:&quot;