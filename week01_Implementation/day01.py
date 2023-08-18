# 문제 1. 운동 중독 플레이어
# 해당 문제는 주어진 수식에 따른 결과를 찾아내는 문제입니다. 소수점을 잘 처리해야 하는 기초적인 수학 문제입니다.
# 구름 레벨 변형 문제입니다.

import math

w, r = map(int, input().split())
result = math.floor(w * ( 1 + r / 30 ))
print(result)
