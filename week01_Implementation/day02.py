# 문제 2. 프로젝트 매니징
# 해당 문제는 정수를 시간 단위로 변환 및 연산하는 문제입니다. 시간을 처리하는 문제는 다양하게 활용될 수 있습니다.
# 구름 레벨 변형 문제입니다.

n = int(input())
t, m = map(int, input().split())

for _ in range(n) :
	c = int(input())
	
	if c < 60 :
		m += c
	else :
		t += c // 60
		m += c % 60

t = (t + m // 60) % 24
m = m % 60

print(t, m)
