def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i])<len(phone_book[i+1]) and phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            return answer
    return answer

# 효율성에서 실패했다.. ㅠㅠ j[0:len(i)]때문이었을까
# sort함수로 한번 정렬을 해주는 풀이를 보았다.