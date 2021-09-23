import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

visit = [[0 for _ in range(N)] for _ in range(N)]
arr = [0]

def bfs(x,y,h):
    queue = deque([(x,y,h)])
    visit[x][y] = 1
    while queue : 
        x,y,h = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < N and ny >=0 and ny < N:
                if graph[nx][ny]- h > 0 and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    queue.append((nx,ny,h))

ans = 1 #비가 안 온경우도 생각해야하는 줄 몰랐다.

for i in range(1,101):
    visit = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if visit[j][k] == 0 and graph[j][k] - i > 0:
                bfs(j,k,i)
                cnt += 1
    ans = max(ans,cnt)

print(ans)
