# 문제 5. 이진수 정렬
# 해당 문제는 주어진 데이터를 조건에 맞게 변형한 후, 다중 조건에 맞추어 정렬하는 문제입니다.
# 현대 모비스 알고리즘 대회 변형 문제입니다.

n, k = map(int, input().split())
num_list = list(map(int, input().split()))

dict_list = []
for num in num_list :
	dict_list.append((num, bin(num)))

sorted_list = sorted(dict_list, key = lambda x:(-x[1].count('1'), -x[0]))
print(sorted_list[k - 1][0])
