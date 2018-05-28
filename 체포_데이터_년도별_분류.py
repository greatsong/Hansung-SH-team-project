import csv

f=open('Arrest_Data_from_2010_to_Present.csv')
a_data=csv.reader(f)
na_data=[]
s_data=[]
next(a_data)

for j in a_data:
    na_data.append(j)

for i in range(2010,2018):

    for row in na_data: #2010년~2017까지 데이터 산출-2018년 1월부터 3월까지는 따로 추출후 리스트에 넣기
        if str(i) in row[1]:
            del row[0]
            del row[1:14]
            s_data.append(row)
f.close()

temp=[]

for i in s_data:
    del i[1]
    i[1]=i[1].replace(' ','')
    i[1]=i[1].replace('(','')
    i[1]=i[1].replace(')','')
    i[1]=i[1].split(',')
    i[1]=[float(j) for j in i[1]]
    temp.append(i)

s_data=[]
s_data=temp
temp=[]

global x_airport1,x_airport2,y_airport1,y_airport2


x_airport1=33.930383
x_airport2=33.959818
y_airport1=-118.441820
y_airport2=-118.370367



def D_zone_include(x,y):
    if x>=x_airport1 and x<=x_airport2 and y>=y_airport1 and y<=y_airport2:
        return True
    else:
        return False

k=0

for row in s_data:
    if D_zone_include(row[1][0],row[1][1])==True:
        temp.append(row)



temp2=[]
temp3=[]
for i in range(2010,2018):
    for row in temp:
        if str(i) in row[0]:
            temp2.append(row)
    temp3.append(temp2)
    temp2=[]


f = open('coordinates.csv', 'w', encoding='utf-8', newline='')
for_wr = csv.writer(f)
for i in temp3:
    for j in i:
        for_wr.writerow(j[1])
f.close()

k=0
month_value=["%.2d" % i for i in range(1,13)]
temp4=[]

for line in temp3:
    for i in month_value:
        for j in range(0,len(line)):
            if i in line[j][0].split('/')[1]:
                k+=1
        temp2.append(k)
        k=0
    temp4.append(temp2)
    temp2=[]
global temp_f
temp_f=[]

for i in temp4:
    for j in range(0,12):
        temp_f.append(i[j])

"""
import matplotlib.pyplot as plt
plt.plot(range(0,96),temp_f,'rs--',color='r')
plt.xticks(range(0,96),a)
plt.grid(True)
plt.show()
"""
