import matplotlib.pyplot as plt
import numpy
import random as r
from 체포_데이터_년도별_분류 import *
from 공항이용객_년도별분류 import *
x = list(range(0,96))
y = [i*90000 for i in temp_f] #체포 데이터
xx=list(range(0,96))
yy=[i*1.5 for i in for_plt_data] #공항 이용객 데이터

def trendline(x_coord,y_coord,color_v,order): #추세선 그리기
    z = numpy.polyfit(x_coord, y_coord, order)
    f = numpy.poly1d(z)
    plt.plot(x,f(x),"r--",color=color_v)

trendline(xx,yy,'orange',4)
trendline(x,y,'green',4)
trendline(xx,yy,'lime',50) #공항이용객

plt.plot(x,y,marker='.',color='r',linewidth=0.4,alpha=0.5,label='Number of arrested people at LA international Airport per month')
plt.plot(xx,yy,marker='.',color='blue',linewidth=0.4,alpha=0.5,label='Number of passengers at LA International Airport per month',)
plt.legend(loc='upper center',bbox_to_anchor=(0.5, 1.1))
plt.savefig('graphwithTline.png',dpi=1000)
plt.xticks(range(0,96),a,rotation=-20)
plt.xlim(-0.3,96)
plt.grid(True)
plt.show()
