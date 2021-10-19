import sys
from collections import deque
INF = sys.maxsize
V,E = map(int,sys.stdin.readline().rstrip().split())
num = int(sys.stdin.readline().rstrip())
visit = [INF for _ in range(V+1)]
graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int,sys.stdin.readline().rstrip().split())
    graph[u].append((v,w))

def solution(x) :
    queue = deque()
    visit[x] = 0
    queue.append((x,0))
    while queue:
        x,w = queue.popleft()
        if w > visit[x]:
            continue
        for i,d in graph[x]:
            if visit[i] > visit[x] + d:
                visit[i] = visit[x] + d
                queue.append((i,d))

solution(num)

for i in visit[1:V+1]:
    if i == INF:
        print("INF")
    else: print(i)