# 문제 13. 발전기 (2)
# 해당 문제는 행렬에서의 효율적 탐색 문제입니다. 발전기 문제와 비슷하지만 완전 탐색의 개념도 필요합니다. 
# 현대 모비스 알고리즘 대회 변형 문제입니다.

n, k = map(int, input().split())
village = []

for _ in range(n) :
	temp = list(map(int, input().split()))
	village.append(temp)

def bfs(x, y, building_type) :
	count = 1
	queue = [[x, y]]
	move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
	
	while len(queue) > 0 :
		x, y = queue.pop(0)
		
		for m in move :
			dx = x + m[0]
			dy = y + m[1]
			
			if dx < 0 or dx >= n or dy < 0 or dy >= n :
				continue
			
			if village[dx][dy] == building_type :
				village[dx][dy] = 0
				queue.append([dx, dy])
				count += 1
	
	return count

result_dict = {}
for i in range(n) :
	for j in range(n) :
		if village[i][j] != 0 :
			building_type = village[i][j]
			village[i][j] = 0
			count = bfs(i, j, building_type)
			
			if count >= k :
				if building_type not in result_dict.keys() :
					result_dict[building_type] = 1
				else :
					result_dict[building_type] += 1

sorted_list = sorted(result_dict.items(), key = lambda x : (-x[1], -x[0]))
print(sorted_list[0][0])
