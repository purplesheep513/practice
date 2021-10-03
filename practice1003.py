# 먼저 start와 destination을 지정해줌
# destination은 다음번의 start가 됨. 갈 수 있는 destination 배열을 뽑아낸다(visited가 되지 않은 곳)
# 배열을 알파벳순으로 sorting한다.
# 그것을 이용해 dfs를 진행한다.
# start와 destination이 겹치면 방문한 것으로 한다.

# 첫 번째로 방문해야할 도시도 계산해줘야 한다 ㅡㅡ
# journey_item에 ICN을 넣고 배열을 뽑아낸 다음, 0번째로 들어있는 배열의 아이템을 찾아온다
# tickets배열안에서 ICN과 찾은 아이템의 index를 알아내고 방문처리 해준다.

def solution(tickets):
    answer = []
    visit = [0 for _ in range(len(tickets))]
    for item in tickets :
        if item[0] == "ICN" and item[1] == journey_item(tickets,"ICN",visit)[0]: # 첫번째로 방문해야 할 배열 가져오기
            visit[tickets.index(item)] = 1
            answer.append(item[0])
            destination = item[1]
            stack = []
            stack.append(destination)

    while stack:
        dest = stack.pop() 
        for i in tickets:
            if len(journey_item(tickets,dest,visit)) > 0:
                new_dest = journey_item(tickets,dest,visit)
                if i[0] == dest and i[1] == new_dest[0] and visit[tickets.index(i)] == 0:
                    visit[tickets.index(i)] = 1
                    answer.append(i[0])
                    stack.append(i[1])
                    break # 방문을 하고나면 다른도시를 출발점으로 다시 돌아준다.
            else: 
                if 0 in visit :
                    answer.append(dest)
                else:
                    answer.append(dest)
                    break

    return answer

def journey_item(tickets,start,visit):
    linked_list = []
    for country in tickets:
        if country[0] == start and visit[tickets.index(country)] == 0:
            linked_list.append(country[1])
    if(len(linked_list)>0):
        linked_list.sort()
    return linked_list

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))