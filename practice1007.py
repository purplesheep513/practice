import sys
from collections import deque

def solution():
    queue = deque()
    queue.append((0,0,0))
    visit[0][0][0] = 1
    while queue:
        x,y,z = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visit[nx][ny][z] == -1 and graph[nx][ny] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    queue.append((nx,ny,z))
                elif z == 0 and visit[nx][ny][z] == -1 and graph[nx][ny] == 1:
                    visit[nx][ny][1] = visit[x][y][z] + 1
                    queue.append((nx,ny,1))


N,M = map(int,sys.stdin.readline().rstrip().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
visit = [[[-1] * 2 for _ in range(M)] for _ in range(N)]


solution()

if visit[N-1][M-1][0] != -1 and visit[N-1][M-1][1] == -1:
    print(visit[N-1][M-1][0])
elif visit[N-1][M-1][0] == -1 and visit[N-1][M-1][1] != -1:
    print(visit[N-1][M-1][1])
else :
    print(min(visit[N-1][M-1][0],visit[N-1][M-1][1]))