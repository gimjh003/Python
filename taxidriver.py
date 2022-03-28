'''
from random import *
guests_dic = {}
possible = 0
for i in range(1, 51):
    guests_dic[i] = randint(5, 50)
for i in guests_dic:
    if guests_dic[i] <= 15:
        print(f"[O] {i}번째 손님 (소요 시간 : {guests_dic[i]}분)")
        possible += 1
    else:
        print(f"[X] {i}번째 손님 (소요 시간 : {guests_dic[i]}분)")
print(f"총 탑승 승객 : {possible}분")
'''

from random import *
cnt = 0
for i in range(1, 51):
    time = randint(5, 50)
    if time <= 15:
        print(f"[O] {i}번째 손님 (소요 시간 : {time}분)")
        cnt += 1
    else:
        print(f"[X] {i}번째 손님 (소요 시간 : {time}분)")
print(f"총 탑승 승객 : {cnt}분")