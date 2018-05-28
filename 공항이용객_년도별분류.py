import csv
f=open('Los_Angeles_International_Airport_-_Passenger_Traffic_By_Terminal.csv')
data=csv.reader(f)

for_save_data=[] #2010년~2018까지 데이터

for row in data:

    for i in range(2010,2019): #2010년~2018까지 데이터 산출
        if str(i) in row[1]:
            del row[0]
            for_save_data.append(row)
f.close()

temp_data=for_save_data
for_save_data=[]

temp=[]

for i in range(2010,2018): #년도별로 month데이터 싹다 모으기
    for row in temp_data:
        if str(i) in row[0].split('/')[2]:
            del row[1:4]
            temp.append(row)
    for_save_data.append(temp)
    temp=[]

temp_data=for_save_data
for_save_data=[]
temp=[]
temp2=[]
month_value=["%.2d" % i for i in range(1,13)]


for i in temp_data: #같은 달 별 분류
    for n in month_value:
        for row in i:
            if n in row[0].split('/')[0]:
                temp.append(row)
        temp2.append(temp)
        temp = []
ab=0
temp3=0
temp4=[] #달별 데이터 저장용 ㅠㅠ
for i in temp2:
    for j in range(0,len(i)):
        temp3+=int(i[j][1])
        k=i[j][0]
    temp4.append([k,temp3])
    temp3=0

for_save_data=temp4 #이 변수에 최종 데이터 저장(format:달/일/년, 이용자 수 ) 이용자수 0인건 데이터가 없을 경우임

global for_plt_data
for_plt_data=[]

for i in for_save_data:
    for_plt_data.append(int(i[1]))


a,b=list(range(1,13)),list(range(1,13))
for i in range(0,8): a+=b;
a=[str(i) for i in a]

"""
import matplotlib.pyplot as plt

plt.xticks(range(0,96),a)
plt.plot(range(0,96),for_plt_data,'rs--',color='blue',linewidth=1,label='Number of passengers at LA International Airport per month',)
plt.legend(loc='upper center',bbox_to_anchor=(0.5, 1.1))
plt.grid(True)
plt.show()

print(len(for_plt_data))
"""

