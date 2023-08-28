# 문제 10. GameJam
# 해당 문제는 시뮬레이션 문제로, 다양한 조건과 요구 사항을 모두 만족하도록 구현해야 합니다.
# 국비 교육 적성고사 변형 문제입니다.

import copy

n = int(input())
xg, yg = map(int, input().split())
xp, yp = map(int, input().split())

board = []
for _ in range(n) :
	temp = input().split()
	board.append(temp)

board_g = copy.deepcopy(board)
count_g = 1
xg, yg = xg - 1, yg - 1
last_pos = board_g[xg][yg]
flag = True
while True :
	how_many = int(last_pos[:-1])
	where = last_pos[-1]
	board_g[xg][yg] = 'x'
	
	for _ in range(how_many) :
		if where == 'U' :
			xg -= 1
			if xg < 0 :
				xg = n - 1
		elif where == 'D' :
			xg += 1
			if xg >= n :
				xg = 0
		elif where == 'R' :
			yg += 1
			if yg >= n :
				yg = 0
		elif where == 'L' :
			yg -= 1
			if yg < 0 :
				yg = n - 1
		
		if board_g[xg][yg] == 'x' :
			flag = False
			break
		else :
			last_pos = board_g[xg][yg]
			board_g[xg][yg] = 'x'
			count_g += 1
	
	if not flag :
		break

count_p = 1
xp, yp = xp - 1, yp - 1
last_pos = board[xp][yp]
flag = True
while True :
	how_many = int(last_pos[:-1])
	where = last_pos[-1]
	board[xp][yp] = 'x'
	
	for _ in range(how_many) :
		if where == 'U' :
			xp -= 1
			if xp < 0 :
				xp = n - 1
		elif where == 'D' :
			xp += 1
			if xp >= n :
				xp = 0
		elif where == 'R' :
			yp += 1
			if yp >= n :
				yp = 0
		elif where == 'L' :
			yp -= 1
			if yp < 0 :
				yp = n - 1
		
		if board[xp][yp] == 'x' :
			flag = False
			break
		else :
			last_pos = board[xp][yp]
			board[xp][yp] = 'x'
			count_p += 1
	
	if not flag :
		break

if count_g > count_p :
	print('goorm', count_g)
else :
	print('player', count_p)
