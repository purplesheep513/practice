def solution(numbers, hand):
    answer = ''
    r_hand = (3,2) # 오른손의 초기 위치
    l_hand = (3,0) # 왼손의 초기 위치

    l_only = [1,4,7]
    r_only = [3,6,9]

    for i in numbers:
        if i in r_only:
            answer += "R"
            r_hand = graph[i]
        elif i in l_only:
            answer += "L"
            l_hand = graph[i]
        else :
            if cal_distance(r_hand,graph[i]) > cal_distance(l_hand,graph[i]):
                answer += "L"
                l_hand = graph[i]
            elif cal_distance(r_hand,graph[i]) < cal_distance(l_hand,graph[i]):
                answer += "R"
                r_hand = graph[i]
            else:
                if hand == "right":
                    answer += "R"
                    r_hand = graph[i]
                elif hand == "left":
                    answer += "L"
                    l_hand = graph[i]
    return answer

graph ={1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), 0:(3,1)}

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand ="right"

def cal_distance(t1,t2):
    nx = t1[0] - t2[0]
    ny = t1[1] - t2[1]
    if nx < 0 :
        nx *= -1
    if ny < 0 :
        ny *= -1
    return nx + ny

print(solution(numbers, hand) == "LRLLLRLLRRL")