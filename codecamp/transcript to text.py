import pyperclip
import copy

import re


message = pyperclip.paste()

# 1: get rid of numbers
stuff = re.compile(r'\n\d\d:\d\d')
mo = stuff.sub('', message)

# 2: get rid of dashes
dashes = re.compile(r'–')
mo = dashes.sub('', mo)

# 3: replace newlines with spaces
spaces = re.compile(r'\n')
aah = spaces.sub(' ', mo)

pyperclip.copy(aah)
print(aah)

