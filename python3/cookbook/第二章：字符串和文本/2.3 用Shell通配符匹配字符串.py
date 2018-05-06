from fnmatch import fnmatch,fnmatchcase

s = fnmatch('foo.txt','*.txt')
print(s)
s = fnmatch('foo.txt','?oo.txt')
print(s)
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

s = [name for name in names if fnmatch(name,'Dat*.csv')]
print(s)

s = fnmatchcase('foo.txt', '*.TXT')
print(s)

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '5122 N CLARK ST',
    '4802 N BROADWAY',
]
from fnmatch import fnmatch,fnmatchcase
s = [add for add in addresses if fnmatchcase(add,'*ST')]
print(s)

s = [addr for addr in addresses if fnmatchcase(addr, '5*[0-9][0-9] *CLARK*')]
print(s)
