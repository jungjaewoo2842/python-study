from random import *
cnt=0 #총 탑승 승객 수
for i in range(1,51): #1~50사이의 승객수
    time=randrange(5,51) #5분~50분 소요시간
    if 5<=time<=15: # 5분~15분 이내의 손님, 탑승승객 수 증가처리
        print("[o] {0}번째 손님 (소요시간 : {1})".format(i,time))
        cnt+=1
    else:#이외 시간의 손님
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(i,time))
print("총 탑승 승객은 {0}".format(cnt))     #총 탑승 승객 수   
