def solution(record):
    dict = {}
    answer = []
    for i in record:
        if "Enter" in i:
            a,b,c = i.split()
            dict[b] = c
        if "Change" in i:
            a,b,c = i.split()
            dict[b] = c
    for i in record:
        if "Enter" in i:
            a,b,c = i.split()
            answer.append(dict[b]+"님이 들어왔습니다.")
        if "Leave" in i:
            a,b = i.split()
            answer.append(dict[b]+"님이 나갔습니다.")

    return answer
