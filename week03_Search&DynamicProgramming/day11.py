# 문제 11. 통증 (2)
# 해당 문제는 통증 문제와는 조건이 다른 문제입니다. 문제를 해결하기 위해서는 동적 프로그래밍의 개념이 필요합니다. 
# 구름 레벨 변형 문제입니다.

n = int(input())
item_list = list(map(int, input().split()))

dp = [1000000] * (n + 1)
dp[0] = 0

for i in range(2) :
	for j in range(item_list[i], n + 1) :
		# (i - k)원을 만드는 방법이 존재하는 경우
		if dp[j - item_list[i]] != 1000000 : 
			dp[j] = min(dp[j], dp[j - item_list[i]] + 1)

if dp[n] == 1000000 :
	print(-1)
else :
	print(dp[n])
	