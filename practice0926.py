import sys
sys.setrecursionlimit(15000)
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    graph=[0]+list(map(int,sys.stdin.readline().rstrip().split()))
    visit = [0 for _ in range(N+1)]
    def dfs(x):
        visit[x] = 1
        if visit[graph[x]] == 0 :
            visit[graph[x]] = 1
            dfs(graph[x])

    cnt = 0
    for i in range(1,N+1):
        if visit[i] == 0:
            dfs(i)
            cnt+=1

    print(cnt)