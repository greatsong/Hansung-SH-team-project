import matplotlib.pyplot as plt
import PIL.Image as pilimg
import csv

#지도 왼쪽 위 : 33.962047, -118.454270
#지도 오른쪽 아래 : 33.913849, -118.360144
#공항 오른쪽 위 : 33.959818, -118.370367
#공항 왼쪽 아래: 33.930383, -118.441820
im = pilimg.open('la지도.png')

x_range=[33.962775,33.913177]#지도 x축 시작과 끝 좌표
y_range=[-118.452951,-118.364310]#지도 y축 시작과 끝 좌표

x_airport = [33.930383,33.959818]#공항(=사각형) x축 시작과 끝 좌표
y_airport = [-118.441820,-118.370367]#공항(=사각형) y축 시작과 끝 좌표

#아래 두개는 위에 좌표이용해서 지도나타내는것임 안건드는걸 추천
x_output=[abs(1.57*(x_airport[0]-x_range[0]))/(x_range[0]-x_range[1]),abs((x_airport[1]-x_range[0]))/(x_range[0]-x_range[1]),abs((x_airport[1]-x_range[0]))/(x_range[0]-x_range[1]),abs(1.57*(x_airport[0]-x_range[0]))/(x_range[0]-x_range[1]),abs(1.57*(x_airport[0]-x_range[0]))/(x_range[0]-x_range[1])]
y_output=[abs((y_airport[1]-y_range[0])/(y_range[0]-y_range[1])),abs((y_airport[1]-y_range[0])/(y_range[0]-y_range[1])),abs(1.57*(y_airport[0]-y_range[0])/(y_range[0]-y_range[1])),abs(1.57*(y_airport[0]-y_range[0])/(y_range[0]-y_range[1])),abs((y_airport[1]-y_range[0])/(y_range[0]-y_range[1]))]
plt.imshow(im,extent = (0,1.57,0,1))#이미지 출력 및 크기 조정
lines = plt.plot(x_output,y_output,linestyle='--')#네모 크기설정
plt.setp(lines, color='brown', linewidth=1.0)#네모 색깔,선두께 설정
plt.title('Crimes around Los Angeles Airport')#이름
x_print = []#출력할 범죄 좌표 받는거 만드는곳
y_print = []#이거도
dummy1 = 0.00 #쓰레기 처리될 숫자들
dummy2 = 0.00
dummy3 = 0.00
dummy4 = []
dummy5 = 0
dummy6 = 0
n = 0
s_print = []
while dummy1 != 157 :
    dummy1 = dummy1 + 1
    while dummy2 != 100  :
        dummy2 = dummy2 + 1
        y_print.append(dummy2/100)
        x_print.append(dummy1/100)
        s_print.append(0)
    dummy2 = -1
finish_x = False#뒤에 끝났는지 확인하는 함수
finish_y = False
while True :
    words = input('원하는 csv파일이름을 입력해주세요.(.csv를 제외하고 입력해주세요.없다면 입력하지 말아주세요)')
    if words == '' :
        break
    if input('원하는 파일명이 '+words+'.csv가 맞습니까?(T/F)') == 'T'  :
        f = open(words+'.csv')
        data = csv.reader(f)
        for row in data :
            finish_x = False#기초작업들
            finish_y = False
            dummy1 = -1
            dummy2 = -1
            dummy5 = abs(1.57*(row[0]-x_range[0]))/(x_range[0]-x_range[1])#퍼센테이지로 변환
            dummy6 = abs(1.57*(row[1]-y_range[0]))/(y_range[0]-y_range[1])
            while finish_x != True :
                dummy1 = dummy1 + 1
                if dummy5 < dummy1/100 and dummy5 >= dummy1/100 : #이번 범위내에 x좌표가 있으면
                    while finish_y != True :
                        dummy2 = dummy2 + 1
                        if dummy6 < dummy2/100 and dummy6 >= dummy2/100 : #이번 범위내에 y좌표가 있으면
                            dummy4 = s_print[dummy1 * 10000 + dummy2 + 1:] #뒷쪽 자르고
                            s_print = s_print[dummy1 * 10000 + dummy2] #앞쪽 놔두고
                            dummy3 = s_print.pop #원하는 곳 꺼내서
                            dummy3 = dummy3 + 1 #크기 1증가
                            s_print.append(dummy3) #증가시킨거 붙이고
                            s_print = s_print + dummy4 #다시 합체
                            finish_x = True#끝남 확인
                            finish_y = True#이것도
                        if dummy2 > 100 :
                            finish_y = True#y좌표 범위 밖인경우 패스
                if dummy1 > 157 :
                    finish_x = True#x좌표 범위 밖인경우 패스
            dummy1 = -1#초기화
            dummy2 = -1
            plt.scatter(x_print, y_print, s = s_print, c = ['r','g','m','c'], alpha = 0.3)
plt.figure(num=1,dpi=1000)
plt.savefig("./test_figure1.png",dpi=1000)