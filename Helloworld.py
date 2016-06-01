from grab import Grab
import json
import HZ
import csv
import urllib
g = Grab(log_file='out.html',user_agent='google')
g.go('https://market.dota2.net/itemdb/current_570.json')
p=g.xpath_text('//*')
table=json.loads(p)
print table
print table['db']
url='https://market.dota2.net/itemdb/'+table['db']
#g.go(url)
#c_id=g.xpath_text('//*')
#v= open('table.csv','w')
#v.write(str(c_id.encode('utf-8')))
#pr=csv.reader(str(c_id.encode('utf-8')),delimiter=";")
resource = urllib.urlopen(url)
out = open('item_table.txt','w')
out.write(resource.read())
out.close()
f =open('id_csv.txt','w')
#v.close()
#for row in pr:
  #      print row
#	f.write(str(row))
ch= csv.reader(open('item_table.txt'),delimiter=';',lineterminator='\r\n')
for row in ch:
	
			HZ.response_message(row[0]+'\t \t'+row[1]+'\t \t'+row[2]+'\t \t'+row[3]+'\t \t'+row[4]+'\t \t'+row[5]+'\t \t'+row[8])
			print (row[0]+'\t \t'+row[1]+'\t \t'+row[2]+'\t \t'+row[3]+'\t \t'+row[4]+'\t \t'+row[5]+'\t \t'+row[8])
			f.write(str(row))
