# 문제 9. 폭탄 구현하기 (2)
# 해당 문제는 폭탄 구현하기 문제에서 조건을 더 추가한 완전 탐색 문제입니다. 요구 사항을 정확히 구현해야 합니다. 
# N사 기출문제를 반영한 문제입니다.

n, k = map(int, input().split())
ground = []

for _ in range(n) :
	temp = input().split()
	
	for i in range(n) :
		if temp[i] == '@' :
			temp[i] = { '@': 0 }
		elif temp[i] != '#' :
			temp[i] = int(temp[i])
		
	ground.append(temp)

bomb_list = []
for _ in range(k) :
	r, c = map(int, input().split())
	bomb_list.append([r, c])

move = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
for bomb in bomb_list :
	x = bomb[0] - 1
	y = bomb[1] - 1
	
	for m in move :
		dx = x + m[0]
		dy = y + m[1]
		
		if dx < 0 or dx >= n or dy < 0 or dy >= n :
			continue
		
		if ground[dx][dy] == '#' :
			continue
		
		if isinstance(ground[dx][dy], dict) :
			ground[dx][dy]['@'] += 2
		else :
			ground[dx][dy] += 1

max_value = 0
for i in range(n) :
	for j in range(n) :
		if ground[i][j] == '#' :
			continue
		
		if isinstance(ground[i][j], dict) :
			compared_value = ground[i][j]['@']
		else :
			compared_value = ground[i][j]
		
		if max_value < compared_value :
			max_value = compared_value

print(max_value)
