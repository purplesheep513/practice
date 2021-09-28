# 원하는 index의 값을 pop해야하는데 그걸 어떻게 해야할지가 에매하다.
# 재귀로 똑같이 구현한 줄 알았는데 재귀로는 안 되고 stack으로 하니까 됐다
# 왜 재귀로는 안 됐을까? 0928 파일을 만들어 재귀 코드를 써보겠다.

import sys

target = int(sys.stdin.readline().rstrip())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))
def dfs():
    cnt = 0
    stack = []
    stack.append((numbers[0],0))
    stack.append((-1*numbers[0],0))
    while stack:
        answer, idx = stack.pop()
        if 0 <= idx+1 < len(numbers):
            stack.append((answer+numbers[idx+1],idx+1))
            stack.append((answer-numbers[idx+1],idx+1))
        elif idx+1 == len(numbers):
            if answer == target:
                cnt +=1
    print(cnt)

dfs()