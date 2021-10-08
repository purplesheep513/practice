import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    n,m = map(int, sys.stdin.readline().rstrip().split())
    graph[n].append(m)
    graph[m].append(n)

def bfs():
    queue = deque()
    queue.append(1)
    parents[1] = 1
    while queue : 
        node = queue.popleft()
        for i in graph[node]:
            if parents[i] == 0:
                parents[i] = node
                queue.append(i)
bfs()

for i in parents[2:]:
    print(i)