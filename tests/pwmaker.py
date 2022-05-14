url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index('.')]
pw = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print(f"{url}의 비밀번호는 {pw}입니다.")