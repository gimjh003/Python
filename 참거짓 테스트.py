'''
xor을 xor 없이 표현하기.
1, 1 = False
0, 0 = False
1, 0 = True
0, 1 = True

a and b = 1, 1일 경우에만 True
a or b = 둘중에 하나라도 1이면 True
not a = 1이면 False, 0이면 True

a and not b = 0, 1일 경우 False. 실패. (1, 0일 경우에만 True)
not a and b = 1, 0일 경우 False. 실패. (0, 1일 경우에만 True)

...잠깐. 어차피 둘 다 같을 때는 False잖아.
만약 2개를 or로 묶어준다면?

(a and not b) or (not a and b)
1,0일 경우 : 성공
0,1일 경우 : 성공
1,1일 경우 : 거짓
0,0일 경우 : 거짓

성공.

두 수가 같을 때만 True?

not a and not b?
0, 0일 경우만 성공.
a and b?
1, 1일 경우만 성공.
(not a and not b) or (a and b)?

더 쉬운 방법.

a == b?
'''
a, b = input().split()
a = int(a)
b = int(b)
c = bool((a and not b) or (b and not a))
print(c)