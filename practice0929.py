import sys

N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]

def dfs(x):
    stack = []
    stack.append(x)
    while stack:
        x = stack.pop()
        for i in range(len(graph[x])):
            if visit[x][i] == 0 and graph[x][i]==1:
                visit[x][i] = 1
                visit[i][x] = 1
                stack.append(i)

cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0 and graph[i][j]==1 :
            visit[i][j] = 1
            dfs(i)
            cnt += 1

print(cnt)