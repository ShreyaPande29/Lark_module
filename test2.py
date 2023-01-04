import re
import datetime
from dateutil.parser import parse

my_str = 'Oct 11 11:27:23 myserver LEEF:2.0|Microsoft|MSExchange|2013 SP1|15345|src=10.50.1.1 dst=2.10.20.20 spt=1200'
# my_str = 'Sep 13 11:23:11 myserver LEEF:1.0|NXLog|identHostName=myserver|Purpose=test"Message=This is a test log message"|SourceModuleNameType=im_file|port 514'

key =["EventReceivedTime",'Hostname','LEEF Version',"Vendor","SourceName","Version","EventID","Data"]
date = re.search("[A-Za-z]+ [0-9]+ [0-9]+:[0-9]+:[0-9]+", my_str).group()
# print(date)

inputs = my_str.split('|')

today = datetime.datetime.now()
date1 =  str(today.year)+' '+date
time = parse(date1).strftime('%Y-%m-%d %H:%M:%S')

str2 =  my_str.replace(date, time)

final = [] 
final.append(time)


arr = [final.append(inputs[i]) for i in range(1,len(inputs)-1) ]        

word =  inputs[-1].replace(" ", ",")

last = dict((a, b) for a, b in (element.split('=') for element in word.split(',')))  
final.append(last)
print(final)