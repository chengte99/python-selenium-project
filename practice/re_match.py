import re
input = '12-12.12'
if re.match('\d\d-\d\d\.\d\d', input):
    print("it matches!")
else:
    print("it doesn't match!")
