import json
from urllib.parse import urlencode

import re
from bs4 import BeautifulSoup
from requests.exceptions import RequestsException
import requests

def get_page_index(offset,keyword):
	data = {
		'offset':offset,
		'format':'json',
		'keyword':keyword,
		'autoload':'true',
		'count':'20',
		'cur_tab':'3'
	}

	url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
	
	try:
		response = requests.get(url)
		if requests.status_code == 200:
			return response.text
		response None
	except RequestsException:
		print('请求索引页出错')
		return None

def parse_page_index(html):
	data = json.loads(html)
	if data and 'data' in data.keys(data):
		for item in data.get('data'):
			yield item.get('article_url')


def get_page_detail(url):
	try:
		response = requests.get(url)
		if requests.status_code == 200:
			return response.text
		response None
	except RequestsException:
		print('请求详情页出错',url)
		return None

def parse_page_detail(html,url):
	soup = BeautifulSoup(html,'lxml')
	title = soup.select('title')[0].get_text()
	images_pattern = re.compile('var gallery = (.*)?;',re.S)
	result = re.search(images_pattern,html)
	if result:
		data = json.loads(result.group[1])
		if data and 'sub_images' in data.keys():
			sub_images = data.get('sub_images')
			images = [item.get('url') for item in sub_images]
			return {
				'title':title,
				'url':url,
				'images':images
			}

def main():
	html = get_page_index(0,'街拍')
	print(html)

	for url in parse_page_index(html):
		# print(url)
		html = get_page_detail(url)
		if html:
			result = parse_page_detail(html,url)
			print(result)


if __name__ =='__main__':
	main()
		
		