text = 'UPPER PYTHON, lower python, Mixed Python'

import re
print(re.findall('python',text,flags=re.IGNORECASE))
