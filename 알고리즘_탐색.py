# 순차 탐색

t = [7, 5, 9, 2, 8]
key = int(input("key : "))
pos = -1
for i in range(len(t)):
    if t[i] == key:
        pos = i
if pos == -1:
    print("해당 키 없음")
else:
    print(pos, "위치에 해당 키 있음")

# 이진 탐색 : 순차 탐색보다 훨씬 빠르지만, 정렬된 데이터에서만 가능하다.
t = [2, 5 ,7, 8, 9]
key = int(input("key : "))
pos = -1

def binary_search(start, end):
    mid = (start+end)/2
    if t[mid] == key:
        return key
    elif start == end: # 키를 찾지 못한 상태에서 마지막 스테이지까지 왔다면
        return -1 # -1(못 찾음) 반환
    elif t[mid] > key:
        return binary_search(start, mid-1)
    else:
        return binary_search(mid+1, end)
    
pos = binary_search(0, len(t))