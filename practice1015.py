import sys

N = int(sys.stdin.readline().rstrip())
def solution(answer):
    if answer < 1:
        return 1
    if answer > 1:
        answer = answer * solution(answer-1)
    return answer

ans = solution(N)

print(ans)