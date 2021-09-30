import sys

def solution(begin, target, words):
    answer = 0
    cnt = 0
    if target not in words:
        return 0
    for i in words:
        if check_word(cnt, i, begin) == 1:
            return
    return answer

def check_word (cnt, word, begin):
    for j in list(word).sort():
        for k in list(begin).sort():
            if j == k :
                cnt += 1
    return cnt


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

solution(begin, target, words)