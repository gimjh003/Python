def RLE(s):
    result = ''
    size = len(s)
    i = 1
    count = 1
    while i < size:
        if s[i] == s[i-1]:
            count += 1
        else:
            result = result + str(count) + s[i-1]
            count = 1
        i += 1
    result = result + str(count) + s[i-1]
    return result

input_str = input()
print("RLE 압축 결과 :", RLE(input_str))