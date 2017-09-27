#coding=utf-8
from xml.dom import minidom

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

dom = minidom.parse('info.xml')

root = dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)

logins = root.getElementsByTagName('login')

for user in logins:
    username = user.getAttribute("username")
    password = user.getAttribute("password")
    print(username, password)

provinces = root.getElementsByTagName('province')
citys = root.getElementsByTagName('city')

for province in provinces:
    print(province.firstChild.data)

for city in citys:
    print(city.firstChild.data)
