# import json
# import re
# x = "Oct 11 11:27:23 myserver LEEF:2.0|Microsoft|MSExchange|2013 SP1|15345|src=10.50.1.1 dst=2.10.20.20 spt=1200"

# print(values)
# key = ['EventReceivedTime','Vendor','SourceName','Version','EventID','Data']
# res = {key[i]: values[i] for i in range(len(key))}
# print(json.dumps(res))
# l = x.split('|')
# print(l)
# print(l[0])


import re 
import json

x = "Oct 11 11:27:23 myserver LEEF:2.0|Microsoft|MSExchange|2013 SP1|15345|src=10.50.1.1 dst=2.10.20.20 spt=1200"

lst = x.split('|')
# print(lst)
import datetime
today = datetime.date.today()
year = today.year
# print(year)
date = re.search("[A-Za-z]+ [0-9]+ [0-9]+:[0-9]+:[0-9]+", lst[0])

res = date.group()

# print(res,'***')

new = lst[0].split(" ")[-2:]
# print(new,'@@@')
new.insert(0,res)
# print(new,'*')
l = lst[1:]
# print(l,'&&')
ab = new + l
print(ab,'###')

key = ['EventReceivedTime','hostname','LEEF Version','Vendor','SourceName','Version','EventID','Data']
res1 = {key[i]: ab[i] for i in range(len(key))}
# print(res1,'**')
# print(json.dumps(res1))