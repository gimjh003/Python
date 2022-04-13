# 퍼셉트론이 대체 뭔데?

x1 = [0,0,1,1] # 첫 번째 입력
x2 = [0,1,0,1] # 두 번째 입력
y = [0,1,1,1] # 입력들의 OR연산 결과

w = [0,0] # 가중치 초기화
b = -1 # 바이어스 초기화
eta = 0.01 # 학습률 초기화

for j in range(100): # 반복하여 학습시키기
    for i in range(len(x1)): # 학습 데이터 수만큼 반복
        f = w[0]*x1[i]+w[1]*x2[i]+b # 퍼셉트론 모델
        w[0] = w[0] + eta*x1[i]*(y[i]-f)
        w[1] = w[1] + eta*x2[i]*(y[i]-f)

print(str(w[0]) + '*x1+'+str(w[1])+'x2'+str(b)) # 퍼셉트론 모델 출력

for i in range(4):
    output = w[0]*x1[i]+w[1]*x2[i]+b
    if output > 0: output = 1
    else: output = 0
    print('input :', x1[i], x2[i], '=> output :', output)