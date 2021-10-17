import sys
from collections import deque

K = int(sys.stdin.readline().rstrip())

for _ in range(K):
    V,E = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(V+1)]
    visit = [[0,True] for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int,sys.stdin.readline().rstrip().split())
        graph[u].append(v)

    def bfs(x):
        queue = deque()
        queue.append(x)
        visit[x] = [1,True]
        while queue:
            x = queue.popleft()
            for i in graph[x]:
                if visit[i][0] == 0 :
                    visit[i][0] = 1
                    if visit[x][1]:
                        visit[i][1] = False
                    else :
                        visit[i][1] = True
                    queue.append(i)
                else :
                    if visit[x][1] == visit[i][1]:
                        return "NO"
        return "YES"

    check = ""
    for i in range(V):
        if visit[i][0] == 0:
            check = bfs(i)
            if check == "NO":
                break
    print(check)