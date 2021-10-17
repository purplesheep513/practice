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
        graph[v].append(u)

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

    check = "YES"
    for i in range(V):
        if visit[i][0] == 0:
            bfs(i)

    for i in range(len(graph)) :
        if check == "YES":
            for j in graph[i]:
                if visit[i][1] == visit[j][1]:
                    check = "NO"
                    break
    print(check)
