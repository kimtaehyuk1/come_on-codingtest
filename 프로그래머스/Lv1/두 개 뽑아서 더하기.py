from itertools import combinations


def solution(numbers):
    answer = set()
    
    for combi in combinations(numbers,2):
        total = sum(combi)
        answer.add(total)

    answer = sorted(answer)


    return answer



numbers = [5,0,2,7]
print(solution(numbers))