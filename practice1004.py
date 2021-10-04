def solution(answers):
    point1 = student1(answers)
    point2 = student2(answers)
    point3 = student3(answers)
    answer = []
    arr = [point1,point2,point3]
    for i in range(3):
        if arr[i] == max(arr):
            answer.append(i+1)
    return answer

def student1(answers):
    point1=0
    for i in range(len(answers)):
        if i%5 == 0:
            if answers[i] == 1:
                point1 +=1
        if i%5 == 1:
            if answers[i] == 2:
                point1 +=1
        if i%5 == 2:
            if answers[i] == 3:
                point1 +=1
        if i%5 == 3:
            if answers[i] == 4:
                point1 +=1
        if i%5 == 4:
            if answers[i] == 5:
                point1 +=1
    return point1

def student2(answers):#2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    point2 = 0
    for i in range(len(answers)):
        if i % 2 == 0:
            if answers[i] == 2:
                point2 += 1
        else:
            if ((i+8)//2) % 4 == 0 :
                if answers[i] == 1:
                    point2 +=1
            else :
                if answers[i] == ((i+8)//2) % 4+2:
                    point2 +=1
    return point2

def student3(answers): #3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
    point3 = 0
    for i in range(len(answers)):
        if i % 10 == 0 or i % 10 == 1:
            if answers[i] == 3:
                point3 += 1
        elif i % 10 == 2 or i % 10 == 3:
            if answers[i] == 1:
                point3 += 1
        elif i % 10 == 4 or i % 10 == 5:
            if answers[i] == 2:
                point3 += 1
        elif i % 10 == 6 or i % 10 == 7:
            if answers[i] == 4:
                point3 += 1
        elif i % 10 == 8 or i % 10 == 9:
            if answers[i] == 5:
                point3 += 1
    return point3

answers = [1,3,2,4,2]
solution(answers)