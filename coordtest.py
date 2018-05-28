import csv
import matplotlib.pyplot as plt

f=open('coordinates.csv')
fe=csv.reader(f)
fw=[]
for k in fe:
    fw.append(k)

x,y=[],[]

for i in fw:
    x.append(float(i[0]))

for j in fw:
    y.append(float(j[1]))

plt.scatter(x,y,s=4,alpha=0.4)
plt.show()