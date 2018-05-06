import urllib.request as request  
import urllib.parse as parse  
import string  
print(""" 
+++++++++++++++++++++++ 
  学校：超神学院 
  专业：德玛班 
  姓名：德玛之力 
  version: python3.2 
+++++++++++++++++=++++ 
     """)  
def baidu_tieba(url, begin_page, end_page):  
    for i in range(begin_page, end_page + 1):  
        sName = './'+str(i).zfill(5)+'.html'  
        print('正在下载第'+str(i)+'个页面, 并保存为'+sName)  
        m = request.urlopen(url+str(i)).read()  
        with open(sName,'wb') as file:  
            file.write(m)  
        file.close()  
if __name__ == "__main__":  
    url = "http://tieba.baidu.com/"  
    begin_page = 1  
    end_page = 3  
    baidu_tieba(url, begin_page, end_page) 