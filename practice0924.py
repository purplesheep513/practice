import sys
from collections import deque
H,W = map(int, sys.stdin.readline().rstrip().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
visit = [[0 for _ in range(W)] for _ in range(H)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque([(x,y)])
    visit[x][y]=1
    if graph[x][y] == "1":
        queue.pop()
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if visit[nx][ny] == 0 and graph[nx][ny]=="0":
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx,ny))

    if visit[H-1][W-1] != 0:
        return visit[H-1][W-1]
    else : return -1

ans = []
for i in range(H):
    for j in range(W):
        if graph[i][j] == "1":
            visit = [[0 for _ in range(W)] for _ in range(H)]
            graph[i][j] = "0"
            ans.append(bfs(0,0))
            graph[i][j] = "1"
        else : ans.append(bfs(0,0))
print(max(ans))
