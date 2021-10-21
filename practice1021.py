import sys
from collections import deque
INF = sys.maxsize

M,N = map(int, sys.stdin.readline().rstrip().split())

graph = []
visit = [[INF for _ in range(M)] for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

def solution():
    queue = deque()
    visit[0][0] = 0
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visit[nx][ny] > visit[x][y] + graph[nx][ny]:
                    visit[nx][ny] = visit[x][y] + graph[nx][ny]
                    queue.append((nx,ny))
solution()
print(visit[N-1][M-1])