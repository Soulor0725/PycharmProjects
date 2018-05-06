import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
     
def parsePage(ilt,html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
		# plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		# tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			price = eval(plt[i].split[":"][1])
			title = eval(tlt[i].split[":"][1])
			ilt.append([price,title])
			# print("====")
	except Exception as e:
		print("parsePage:{}".format(e))	
		print(" ")
				
def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:6}\t"
	print(tplt.format("序号","价格","商品名称"))
	count = 0
	for g in ilt:
		count = count+i
		print(tplt.format(count,g[0],g[1]))


def main():
	goods = "书包"
	depth = 2
	start_url = "https://s.taobao.com/search?q=" + goods
	infoList = []
	for i in range(depth):
		try:
			url = start_url + "&s=" + str(44*i)
			html = getHTMLText(url)
			# print("====")
			# print(html)
			parsePage(infoList,html)
		except Exception as e:
			print("main:{}".format(e))	
			continue

	printGoodsList(infoList)			

main()	
