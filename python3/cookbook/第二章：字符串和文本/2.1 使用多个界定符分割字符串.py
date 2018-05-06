line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
s = re.split(r'[;,\s]\s*',line)
print(s)