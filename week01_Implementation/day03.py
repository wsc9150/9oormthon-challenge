# 문제 3. 합 계산기
# 해당 문제는 문자열과 정수가 혼용된 데이터를 적절하게 분리한 후, 부호를 기준으로 모든 결과를 합산하는 문제입니다.
# W사의 코딩 테스트 변형 문제입니다.

import math

t = int(input())
result = 0

for _ in range(t) :
	a, op, b = input().split()
	
	if op == '+' :
		result += int(a) + int(b)
	if op == '-' :
		result += int(a) - int(b)
	if op == '*' :
		result += int(a) * int(b)
	if op == '/' :
		result += math.floor(int(a) / int(b))

print(result)
