def solution(s):
    splited_string = ''
    answer = len(s)
    for i in range(1,len(s)):
        splited_string = split_string(s,i)
        result = ''
        cnt = 1
        for i in range(0,len(s),len(splited_string)):
            if i <= len(s)-2 * len(splited_string):
                if s[i:i+len(splited_string)] == s[i+len(splited_string):i + 2 * len(splited_string)]:
                    cnt += 1
                else : 
                    if cnt != 1:
                        result += str(cnt) + s[i:i+len(splited_string)]
                        cnt = 1
                    else : 
                        result += s[i:i+len(splited_string)]
            else : 
                if len(s) - i >= len(splited_string) :
                    if cnt != 1:
                        result += str(cnt) + s[i:len(s)]
                        cnt = 1
                    else : 
                        result += s[i:len(s)]
        answer = min(len(result), answer)
        print(result)
    return answer

def split_string(s,i):
    s = s[0:i]
    return s

s = "a"

print(solution(s))