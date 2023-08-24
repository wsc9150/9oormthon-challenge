# 문제 6. 문자열 나누기
# 해당 문제는 문자열을 분리하는 모든 경우의 수를 조합으로 탐색한 후, 조건에 따라서 점수를 측정하는 완전 탐색 문제입니다. 
# 신규 제작 문제입니다.

n = int(input())
s = input()
part_str_list = []
sorted_list = []

for i in range(1, n - 1) :
	for j in range(i + 1, n) :
		part_str_list.append([s[0:i], s[i:j], s[j:n]])
		sorted_list.extend([s[0:i], s[i:j], s[j:n]])

sorted_list = sorted(list(set(sorted_list)))

result = []
for l in part_str_list :
	sum_value = 0
	
	for i in l :
		sum_value += sorted_list.index(i) + 1
	
	result.append(sum_value)

print(max(result))
