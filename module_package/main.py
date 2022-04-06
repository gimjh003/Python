# 패키지 내부의 모듈을 읽어 들입니다.
'''
import test_package.module_a as a
import test_package.module_b as b
'''
# 모듈 내부의 변수를 출력합니다.
from test_package import *
print(module_a.variable_a)
print(module_b.variable_b)