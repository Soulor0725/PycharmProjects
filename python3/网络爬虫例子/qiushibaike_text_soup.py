import requests
from bs4 import BeautifulSoup
import re

def crawl_joke_list_use_bs4(page=1):
    url = 'https://www.qiushibaike.com/text/page/'+str(page)
    
    res = requests.get(url)

    soup = BeautifulSoup(res.text,'html5lib')

    joke_list = soup.find_all("div",class_=re.compile("article block untagged mb15"))

    for child in joke_list:

        user_name = child.find('h2').string
        content = child.find('span')

        string_joke = user_name+'\t'+"".join(content.stripped_strings)
        print(string_joke)


if __name__ == '__main__':
    # crawl_joke_list_use_bs4(1)    
    for i in range(1,10):
        print(i)
        crawl_joke_list_use_bs4(i)        