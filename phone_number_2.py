import re

phoneNumRegex = re.compile(r'\d\d-\d\d\d-\d\d\d\d') # looking for pattern
mo = phoneNumRegex.search('Call me at 415-555-1011 tomorrow, or at 415-555-9999') # regular expression object
print (mo.group()) # match object
