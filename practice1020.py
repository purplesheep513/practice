import sys
from collections import deque
INF = sys.maxsize
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
visit = [INF for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v, w = map(int,sys.stdin.readline().rstrip().split())
    graph[u].append((v,w))
FR, TO = map(int,sys.stdin.readline().rstrip().split())

def solution(x):
    queue = deque()
    queue.append((x,0))
    visit[x] = 0
    while queue:
        x,w = queue.popleft()
        if w > visit[x]:
            continue
        for i,d in graph[x]:
            if visit[i] > visit[x] + d:
                visit[i] = visit[x] + d
                queue.append((i,d))

solution(FR)

print(visit[TO])
