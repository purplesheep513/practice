import sys

def solution(begin, target, words):
    answer = 0
    cnt = 0
    if target not in words:
        return 0
    for i in range(len(words)):
        print(words[i])
        # for j in list(words[i]).sort():
        #     for k in list(begin).sort():
        #         if j == k :
        #             cnt += 1
    
    # print(cnt)
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

solution(begin, target, words)