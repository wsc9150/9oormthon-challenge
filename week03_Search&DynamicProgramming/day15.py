# 문제 15. 과일 구매
# 해당 문제는 그리디의 응용문제입니다. 현재 상태에서 최고의 선택을 찾아야 합니다. 
# 국비 교육 적성고사 변형 문제입니다.

n, k = map(int, input().split())
fruit_list = []

for _ in range(n) :
	temp = list(map(int, input().split()))
	fruit_list.append(temp)

fruit_list = sorted(fruit_list, key = lambda x : x[1] // x[0])

result = 0
while len(fruit_list) > 0 :
	p, c = fruit_list.pop()
	
	if k >= p :
		result += c
		k -= p
	else :
		result += (c // p) * k
		break
	
print(result)
