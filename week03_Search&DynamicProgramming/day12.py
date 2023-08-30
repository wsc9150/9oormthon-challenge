# 문제 12. 발전기
# 해당 문제는 행렬에서의 효율적 탐색 문제입니다. 탐색을 하는 기본 틀은 같지만, 항상 탐색 조건을 잘 설정해야 합니다. 
# 구름 레벨 변형 문제입니다.

n = int(input())
village = []

for _ in range(n) :
	temp = list(map(int, input().split()))
	village.append(temp)

def bfs(x, y) :
	queue = [[x, y]]
	move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	
	while len(queue) > 0 :
		x, y = queue.pop(0)
		
		for m in move :
			dx = x + m[0]
			dy = y + m[1]
			
			if dx < 0 or dx >= n or dy < 0 or dy >= n :
				continue
			
			if village[dx][dy] == 1 :
				village[dx][dy] = 0
				queue.append([dx, dy])

result = 0
for i in range(n) :
	for j in range(n) :
		if village[i][j] == 1 :
			village[i][j] = 0
			bfs(i, j)
			result += 1

print(result)
