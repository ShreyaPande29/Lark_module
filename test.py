import json
from dateutil.parser import parse
import datetime



def is_date(string, fuzzy=False):
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

my_str = 'Oct  11:27:23 myserver LEEF:2.0|Microsoft|MSExchange|2013 SP1|15345|src=10.50.1.1 dst=2.10.20.20 spt=1200'
# my_str = 'Sep 13 11:23:11 myserver LEEF:1.0|NXLog|identHostName=myserver|Purpose=test"Message=This is a test log message"|SourceModuleNameType=im_file|port 514'

key =["EventReceivedTime",'Hostname','LEEF Version',"Vendor","SourceName","Version","EventID","Data"]
# date = re.search("[A-Za-z]+ [0-9]+ [0-9]+:[0-9]+:[0-9]+", a[0]).group()
# print(date)

inputs = my_str.split('|')

# print(inputs)
d = []
c=''

for i in inputs[0].split():
    if is_date(i):
        c+=" "+''.join(i)

    else:
        d.append(i)

# obj = [c=c+" "+''.join(i) if is_date(i) else d.append(i) for i in inputs[0].split()]

today = datetime.datetime.now()
date =  str(today.year) +c
time = parse(date).strftime('%Y-%m-%d %H:%M:%S')

d.insert(0,time)
final = [] 
final.extend(d)

arr = [final.append(inputs[i]) for i in range(1,len(inputs)-1) ]        

word =  inputs[-1].replace(" ", ",")

last = dict((a, b) for a, b in (element.split('=') for element in word.split(',')))  
final.append(last)

# json_output =json.dumps(dict(zip(key, final)))
json_output =dict(zip(key, final))

from lark import Lark

# l = Lark('''start: WORD "," WORD "!"

#             %import common.WORD   
#             %ignore " "           
#          ''')

print(key,final)

# print( l.parse(key, final) )

# print(json_output)

