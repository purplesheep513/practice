def solution(participant, completion):
    answer = ''
    for i in participant:
        if i not in completion :
            answer = i
        else:completion.remove(i)
    return answer