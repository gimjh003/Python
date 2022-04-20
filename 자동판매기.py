price = int(input("물건값을 입력하세요 : "))
otdw = int(input("1000원 지폐개수 : "))*1000
fhdw = int(input("500원 지폐개수 : "))*500
ohdw = int(input("100원 지폐개수 : "))*100
price -= otdw+fhdw-ohdw
price *= -1
fhdw = price//500
price -= fhdw*500
ohdw = price//100
price -= ohdw*100
tw = price//10
price -= tw*10
ow = price//1
price -= ow
print(f"500원 = {fhdw} 100원 = {ohdw} 10원 = {tw} 1원 = {ow}")