from datetime import datetime

dateFormatter = "%Y, %B %d, %A, %H:%M:%S"

def solution(lines):
    print(datetime.strptime(lines[0],dateFormatter) - lines[1].replace("s",""))
    answer = 0
    return answer

lines = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

solution(lines)