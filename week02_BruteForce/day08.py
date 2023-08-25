# 문제 8. 통증
# 해당 문제는 그리디의 기초가 되는 문제입니다. 현재 상태에서 최고의 선택을 찾아야 합니다. 
# 구름 레벨 변형 문제입니다.

n = int(input())
result = 0

result += n // 14
n = n % 14

result += n // 7
n = n % 7

result += n // 1

print(result)
