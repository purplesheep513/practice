def solution(s):
    splited_string = ''
    for i in range(1,len(s)):
        splited_string = split_string(s,i)
        for i in range(0,len(s),len(splited_string)):
            print(s[i:i+len(splited_string)])
            
    answer = 0
    return answer

def split_string(s,i):
    s = s[0:i]
    return s

s = "aabbaccc"

solution(s)