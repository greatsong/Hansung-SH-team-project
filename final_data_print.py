from 체포_데이터_년도별_분류 import *
from 공항이용객_년도별분류 import *


a,b=list(range(1,13)),list(range(1,13))
for i in range(0,8): a+=b;
a=[str(i) for i in a]

temp_f=[i*90000 for i in temp_f]
for_plt_data=[i*1.5 for i in for_plt_data]
import matplotlib.pyplot as plt

plt.plot(range(0,96),temp_f,marker='^',color='r',linewidth=0.4,label='Number of arrested people at LA international Airport per month')
plt.plot(range(0,96),for_plt_data,marker='^',color='blue',linewidth=0.4,label='Number of passengers at LA International Airport per month',)
plt.xticks(range(0,96),a)
plt.legend(loc='upper center',bbox_to_anchor=(0.5, 1.1))
plt.grid(True)
plt.savefig('Finally_I_did_it!',dpi=1000)
plt.show()