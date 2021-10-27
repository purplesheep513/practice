import math

def solution(progresses, speeds):
    answer = []
    re_def = []
    cnt = 0
    for i in range(len(progresses)):
        re_def.append(math.ceil((100-progresses[i])/speeds[i]))

    
    while True:
        if cnt ==len(progresses):
            break
        temp = re_def[cnt]
        a = 0
        for i in range(cnt,len(progresses)):
            re_def[i] -= temp
        for i in re_def[cnt:len(progresses)]:    
            if i <=0:
                a +=1
            else:
                break
        answer.append(a)
        cnt += a
    return answer

progresses= [93, 30, 55]
speeds= [1, 30, 5]
print(solution(progresses, speeds))