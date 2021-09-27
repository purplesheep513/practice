import sys

target = int(sys.stdin.readline().rstrip())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))
visit = [[0 for _ in range(len(numbers))] for _ in range(len(numbers))]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = []
for i in range(len(numbers),0,-1):
    graph.append([numbers[j] for j in range(i)])

def dfs(x,y):
    answer = 0
    visit[x][y] = 1
    stack = []
    stack.append((x,y,answer))
    while stack:
        x,y,answer = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < len(graph[x]) and 0<=ny < len(graph[y]):
                if visit[nx][ny] == 0 :
                    visit[nx][ny] = 1
                    if dx[i] == 0 :
                        answer += graph[nx][ny] * dy[i]
                        stack.append((nx,ny,answer))
                        print(answer)
                    if dy[i] == 0:
                        answer += graph[nx][ny] * dx[i] 
                        stack.append((nx,ny,answer))
                        print(answer)
dfs(0,0)