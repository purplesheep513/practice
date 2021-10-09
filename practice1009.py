import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N,M,K = map(int,sys.stdin.readline().rstrip().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]
    visit = [[0 for _ in range(N)] for _ in range(M)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for _ in range(K):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        graph[y][x] = 1

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        visit[x][y] = 1
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N :
                    if visit[nx][ny] == 0 and graph[nx][ny] == 1:
                        visit[nx][ny] = 1
                        queue.append((nx,ny))
    cnt = 0
    for i in range(M):
        for j in range(N):
            if visit[i][j] == 0 and graph[i][j] ==1:
                bfs(i,j)
                cnt += 1

    print(cnt)