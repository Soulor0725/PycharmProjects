# import tensorflow as tf

# print(tf.__version__)
# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))


import requests
import re

content = requests.get('https://book.douban.com/').text
pattern = re.compile('<div class="more-meta">.*?<h4 class="title">(.*?)</h4>.*?"author">(.*?)</span>.*?"year">(.*?)</span>.*?publisher">(.*?)</span>.*?</div>',re.S)
results = re.findall(pattern,content)
for result in results:
    print('title:'+result[0].strip()+\
        '->author:'+result[1].strip()+\
        '->year:'+result[2].strip()+\
        '->publisher:'+result[3].strip())