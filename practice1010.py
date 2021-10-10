def solution(lottos, win_nums):
    lottos.sort()
    cnt = 0
    cnt_zero = 0
    answer = []

    for i in lottos:
        if i == 0:
            cnt_zero +=1
        else:
            if i in win_nums:
                cnt +=1

    if cnt < 2:
        if cnt == 0 and cnt_zero==0:
            answer.append(6)
        else :answer.append(7-cnt-cnt_zero)
        answer.append(6)
    else:
        answer.append(7-cnt-cnt_zero)
        answer.append(7-cnt)
    return answer

lottos = [2, 3, 4, 5, 7, 8]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))