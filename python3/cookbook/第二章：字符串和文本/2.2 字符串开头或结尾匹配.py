filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('s'))

import os
filenames = os.listdir('.')
filenames = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
print(filenames)

s = [name for name in filenames if name.endswith(('c','h'))]
print(s)