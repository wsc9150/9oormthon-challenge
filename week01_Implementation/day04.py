# 문제 4. 완벽한 햄버거 만들기
# 해당 문제는 정렬을 활용해서 주어지는 값들이 올바르게 배치되어 있는지 확인하는 문제입니다.
# 국내 알고리즘 경진대회 변형 문제입니다.

n = int(input())
k_list = list(map(int, input().split()))

result = 0
up_down = ''
for i in range(len(k_list) - 1) :
	if k_list[i + 1] - k_list[i] > 0 :
		up_down += '+'
	elif k_list[i + 1] - k_list[i] < 0 :
		up_down += '-'
	
	result += k_list[i]

result += k_list[-1]

if '+' in up_down.lstrip('+') :
	print(0)
else :
	print(result)
