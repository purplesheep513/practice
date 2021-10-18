import sys
from collections import deque
N,M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]
dis = [0 for _ in range(N+1)]

for i in range(1,M+1):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    graph[n].append(m)
    graph[m].append(n)

def bfs(x):
    queue = deque()
    if visit[x] == 0:
        visit[x] = 1
        queue.append(x)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] += visit[x] + 1
                queue.append(i)

kevin = 10000
for i in range(1,N+1):
    if visit[i] == 0:
        bfs(i)
        for j in range(1,N+1):
            if i != j:
                dis[j] = dis[j] + visit[j]
        visit = [0 for _ in range(N+1)]
print(dis.index(min(dis[1:N+1])))