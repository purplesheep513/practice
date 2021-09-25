# 어쨌든 bfs가 H,W 까지 가기만 하면 되는것이다.
# 모든 경우를 다 돌려봐야한다.
# 어렵다 더 생각해봐야겠다.

import sys
from collections import deque
H,W = map(int, sys.stdin.readline().rstrip().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
visit = [[[0]*2 for _ in range(W)] for _ in range(H)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    queue = deque([(0,0,1)])
    visit[0][0][1] = 1
    while queue:
        x,y,w = queue.popleft()
        if x == H-1 and y == W-1 :
            return visit[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if graph[nx][ny]=="1" and w ==1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    queue.append((nx,ny,0))
                elif graph[nx][ny]== "0" and visit[nx][ny][w]==0:
                    visit[nx][ny][w] == visit[x][y][w] + 1
                    queue.append((nx,ny,w))
        return -1


print(bfs())