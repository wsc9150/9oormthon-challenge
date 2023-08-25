# 문제 7. 구름 찾기 깃발
# 해당 문제는 행렬에서 문제의 요구 사항을 만족하는 값을 찾는 완전 탐색 문제입니다. 행렬에서의 이동 개념이 필요합니다. 
# 구름 레벨 변형 문제입니다.

n, k = map(int, input().split())
board = []

for _ in range(n) :
	temp = list(map(int, input().split()))
	board.append(temp)

move = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
result = 0

for i in range(n) :
	for j in range(n) :
		flag = 0
		
		for m in move :
			# 현재 자리가 깃발인 경우
			if board[i][j] == 1 :
				continue
			
			# 게임판 밖인 경우
			if i + m[0] < 0 or i + m[0] >= n or j + m[1] < 0 or j + m[1] >= n :
				continue
			
			if board[i + m[0]][j + m[1]] == 1 :
				flag += 1
		
		if flag == k :
			result += 1

print(result)
