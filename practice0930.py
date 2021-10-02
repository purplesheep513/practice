# 나의 생각은 이것이었다.
# 1. 글자가 하나만 겹치면 연결된 노드로 간주한다
# 2. 그대로 BFS를 진행한다

import sys
from collections import deque

def find_linked(word,words): # 해당 단어와 같은 글자가 하나뿐인 단어들을 가져오는 리스트 생성
    cnt = 0
    linked_node = []

    for i in words:
        for j in range(len(list(i))):
            if i[j]==word[j]:
                cnt += 1   
        if cnt == len(word)-1:
            linked_node.append(i)
        cnt = 0 
    
    return linked_node

def solution(begin, target, words):
    answer = 0

    if target not in words: # target이 없으면 return 0
        return answer

    queue = deque([begin]) #queue에 처음 담을 단어와 answer을 넣어줌.
    visit = [0 for _ in range(len(words))] #visit는 words배열을 기반으로 한다.
    while queue:
        word = queue.popleft()
        linked_nodes = find_linked(word,words)
        for i in linked_nodes: #단어에 따른 관련 노드 리스트를 돈다.
            if visit[words.index(target)] == 0:
                if word == begin:
                    visit[words.index(i)] += 1
                else : visit[words.index(i)] += visit[words.index(word)] + 1
                queue.append((i))
    
    return visit[words.index(target)]

# 헐 풀었다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11