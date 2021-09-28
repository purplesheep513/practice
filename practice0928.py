import sys

target = int(sys.stdin.readline().rstrip())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))
cnt = 0
def dfs(idx, answer):
    global cnt
    if idx + 1 == len(numbers):
        if answer == target:
            cnt += 1
    elif 0<= idx+1 < len(numbers):
        dfs(idx+1,answer + numbers[idx+1])
        dfs(idx+1,answer - numbers[idx+1])

dfs(-1,0)

print(cnt)

# 되네..