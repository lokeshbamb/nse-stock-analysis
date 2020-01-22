import os, sys
import pandas as pd
import datetime
import requests
import requests, zipfile, io
article_read = pd.read_csv('EQUITY_L.csv')
company = []
x = datetime.datetime.now()
for k in range(0,1635,1):
 df = article_read.iloc[[k]]
 s = str(df[['SYMBOL']])
 #print(len(s))
 #print(s)
 l = list(s.split())
 company.append(l[2])
n = 1
j = 1
print(company)
while n>0:
 try:
    day = x - datetime.timedelta(days=j)
    m = day.strftime("%b")
    y = day.strftime("%Y")
    d = day.strftime("%d")
    fnamer = 'cm' + d + m.upper() + y + 'bhav.csv'
    surlid = 'https://www1.nseindia.com/content/historical/EQUITIES/' + y +'/' + m.upper() + '/' + fnamer + '.zip'
    r = requests.get(surlid)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    article_read = pd.read_csv('/home/lokesh/ML/Market/' + fnamer)
    n -=1
    print(n)
    j +=1
    z = 0
    #l[11] = symbol
    #l[last] = close
 except:
   pass

#print(company)
if(n==0):
 for i in company:
  try:
     #We read the existing text from file in READ mode
     print(i)
     s = str(article_read[article_read.SYMBOL == i][['TIMESTAMP','CLOSE']])
     a = s.split(' ')
     #print(s)
     l = list(a)
     l = list(filter(None, l))
     #print(l)
     zzz = float(l[-1]) 
     outs = l[-2] + "," + l[-1] + "\n"
     #src=open(i + ".csv","r")
     #fline=outs    #Prepending string
     #oline=src.readlines()
     #Here, we prepend the string we want to on first line
     #oline.insert(0,fline)
     #src.close()
    #We again open the file in WRITE mode for deleting rows
     src=open(i + ".csv","w")
     src.writelines(oline)
     src.close()
     readFile = open(i + ".csv")
     lines = readFile.readlines()
     readFile.close()
     w = open(i + ".csv",'w')
     w.writelines([item for item in lines[1:]])
     w.close()
     #print(outs)
  except:
     pass
