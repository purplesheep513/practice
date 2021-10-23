key = [("zero","0"),("one","1"),("two","2"),("three","3"),("four","4"),("five","5"),("six","6"),("seven","7"),("eight","8"),("nine","9")]

def solution(s):
    answer = ""
    for i,j in key:
        s = s.replace(i,j)
    answer = s
    return int(answer)
