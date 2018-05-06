text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.find('no'))


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')    

if re.match(r'[?*?]+/\d+/\d+', text2):
    print('yes')
else:
    print('no')    


datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')    
else:
    print("no")    

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
s = datepat.findall(text)
print(s)