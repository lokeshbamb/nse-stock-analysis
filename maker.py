import datetime
import pandas as pd
article_read = pd.read_csv('EQUITY_L.csv')
company = []
x = datetime.datetime.now()
for k in range(250,324,1):
 df = article_read.iloc[[k]]
 s = str(df[['SYMBOL']])
 #print(len(s))
 #print(s)
 l = list(s.split())
 company.append(l[2])
for i in company:
  file1 = open(i+".csv","a")
  print(i)
  j = 0
  n = 365 
  z = 0
  while n>0:
   try:
    day = x - datetime.timedelta(days=j)
    m = day.strftime("%b")
    y = day.strftime("%Y")
    d = day.strftime("%d")
    fnamer = 'cm' + d + m.upper() + y + 'bhav.csv'
    #surlid = 'https://www1.nseindia.com/content/historical/EQUITIES/' + y +'/' + m.upper() + '/' + fnamer + '.zip'
    #r = requests.get(surlid)
    #z = zipfile.ZipFile(io.BytesIO(r.content))
    #z.extractall('/home/lokesh/ML/Market')
    article_read = pd.read_csv('/home/lokesh/ML/Market/' + fnamer)
    s = str(article_read[article_read.SYMBOL == i][['TIMESTAMP','CLOSE']])
    a = s.split(' ')
    #print(s)
    l = list(a)
    l = list(filter(None, l))
    zzz = float(l[-1]) 
    outs = l[-2] + "," + l[-1] + "\n"
    #print(outs)
    file1.write(outs)
    #costs.append(float(l[len(l)-1]))
    #mdate.append(day.strftime("%x"))
    n -=1
    print(n)
    j +=1
    z = 0
    #l[11] = symbol
    #l[last] = close
    print(i)
   except:
    j +=1  
    print(n)
    z+=1
    if(z==10):
      break 

  file1.close() 



