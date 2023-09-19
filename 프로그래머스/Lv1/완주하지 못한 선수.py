# def solution(participant, completion):
#     answer = ''

#     for i in completion:
#         participant.remove(i)

#     answer += participant[0]


#     return answer


def solution(participant, completion):

    # 우선 정렬시키기
    participant.sort()
    completion.sort()

    # for zip을 통해 만약 중간에 다른것이 있으면 i출력, 근데 다른게 중간에 안나오면 parti 맨 마지막에 있는게 답이다.
    for i,j in zip(participant,completion):
        if i != j:
            return i
        

    return participant[-1]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = 	["stanko", "ana", "mislav"]
print(solution(participant,completion))