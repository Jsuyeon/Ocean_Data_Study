##Jsuyeon##
#제가 살고 있는 부산의 2021/02/09의 수온과 염분 자료를 plot하는 연습을 해보았습니다
import numpy as np
with open('C:\\Users\\soy19\\Downloads\\부산_2021-02-09.txt') as data:
    f=data.readlines()

temp=[]
salt=[]
date=[]

for data in f:
    temp.append(data.split()[3])
    salt.append(data.split()[4])
    date.append(data[0:16])
temp=np.array(temp)
salt=np.array(salt)


from datetime import datetime
import matplotlib.pyplot as plt

DATE=[]
for row in date:
    date_split=datetime.strptime(row,'%Y-%m-%d %H:%M')
    DATE.append(date_split)

#creae figrue
fig,ax=plt.subplots(1)
plt.xlabel('Date')
plt.ylabel('Temperature',color='b',alpha=0.8)
maxi_temp=max(temp)

ax.plot(DATE,temp,'b-')
ax.set_ylim(ax.get_ylim()[::-1])
plt.title('Temperature and Salinity(BUSAN,KOREA 20210209) from KOOFS')


fig.autofmt_xdate(rotation=50)
plt.twinx()
plt.ylabel('Salinity',color='r')
maxi_sal=max(salt)
plt.plot(DATE,salt,'r-',alpha=0.8)

plt.show()
