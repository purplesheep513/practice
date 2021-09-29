def bfs(n, computers):
    visit = [[0 for _ in range(n)] for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and computers[i][j]==1 :
                stack = []
                stack.append(i)
                while stack:
                    x = stack.pop()
                    for k in range(len(computers[x])):
                        if visit[x][k] == 0 and computers[x][k]==1:
                            visit[x][k] = 1
                            visit[k][x] = 1
                            stack.append(k)
                answer += 1
    return answer