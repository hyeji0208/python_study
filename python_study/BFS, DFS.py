from collections import deque

graph = {
  0: [1, 3, 6],
  1: [0, 3],
  2: [3],
  3: [0, 1, 2, 7],
  4: [5],
  5: [4, 6, 7],
  6: [0, 5],
  7: [3, 5]
}

#BFS
start_v = 0

def bfs(graph, start_v):
  # 초기 설정
  q = deque()
  visited = {}
  # 시작점 예약
  q.append(start_v)
  visited[start_v] = True

  while q:
    # 방문
    cur_v = q.popleft()
    # 다음 노드 예약
    for next_v in graph[cur_v]:
      if next_v not in visited:
        q.append(next_v)
        visited[next_v] = True

bfs(graph, start_v)

#DFS
visited = {}

def dfs(cur_v):
  # 방문
  visited[cur_v] = True
  print(cur_v)
  # 다음 노드 dfs()
  for next_v in graph[cur_v]:
    if next_v not in visited:
      dfs(next_v)

dfs(0)