name = []
avg = []
with open('excel.txt', 'r') as file:
    file.readline() # 분류 스킵
    while True: # 모든 사람을 읽어들임
        temp = file.readline().split() #이름과 점수들을 리스트 형태로 만듦.
        if temp==[]: # temp가 []면 모든 사람을 읽은 상태이므로 while문에서 벗어난다.
            f = open('excel-result.txt', 'w') # 결과 파일 작성
            f.write('이름\t평균\n')
            for n in name:
                f.write("{}\t{}\n".format(n, avg[name.index(n)])) # 이름과 점수는 공통돤 인덱스 값을 가진다.
            f.close()
            break
        name.append(temp[0]) # 이름
        total = int(temp[1])+int(temp[2])+int(temp[3])+int(temp[4])
        avg.append(total/4)
        
'''
IndexError : list index => if temp==[]로 해결
'''
