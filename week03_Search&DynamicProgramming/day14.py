# 문제 14. 작은 노드
# 해당 문제는 그래프와 노드, 간선에 대한 개념이 필요한 문제입니다. 현재 위치한 노드에서 다른 노드로 이동하는 개념이 필요합니다. 
# 신규 제작 문제입니다.

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m) :
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

for arr in graph :
	arr.sort()
	
visited = [False for _ in range(n + 1)]
visited[k] = True
count = 1
result = 0

while True :
	for node in graph[k] :
		if not visited[node] :
			k = node
			count += 1
			visited[node] = True
			break
	else :
		result = k
		break
		
print(count, result)
