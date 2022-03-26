price = int(input("물건값을 입력하시오 : "))
money10 = int(input("1000원 지폐개수 : "))*1000
money5 = int(input("500원 동전개수 : "))*500
money1 = int(input("100원 동전개수 : "))*100
price -= (money10+money5+money1)
if(price>0):
    print("돈이 부족합니다.")
elif(price==0):
    print("받을 수 있는 거스름돈이 없습니다.")
else:
    price = -price
    print('거스름돈 : {}원'.format(price))
