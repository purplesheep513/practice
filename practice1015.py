import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
X,Y = map(int, sys.stdin.readline().rstrip().split())
T = int(sys.stdin.readline().rstrip())
visit = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for _ in range(T):
    n,m = map(int, sys.stdin.readline().rstrip().split())
    graph[n].append(m)
    graph[m].append(n)

def bfs(x,y):
    queue = deque([x])
    visit[x] = 1
    while queue : 
        x = queue.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] += visit[x] +1
                queue.append(i)
    return visit[y]

print(bfs(X,Y)-1)