# 문제 url : https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    # 시간 초과
    # def part_fib_sum(m):
    #     results_lists = []
    #     for i in range(len(elements)): i ~> 0 ~ 4 
    #         result_sum = 0
    #         for j in range(i, i+m):  
    #             result_sum += elements[j % len(elements)]
    #         results_lists.append(result_sum)

    #     results_lists = list(set(results_lists))
    #     return results_lists

    # answer = 0
    # results = []
    # for i in range(1, len(elements) + 1):
    #     results += part_fib_sum(i)

    # answer = len(set(results))

    answer = 0
    init_len = len(elements)

    # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
    elements = elements * 2
    result_lists = set()

    def part_fib_sum2(m):
        for i in range(init_len):
            result_lists.add(sum(elements[i:i+m]))

    for i in range(1, init_len+1):
        part_fib_sum2(i)

    answer = len(result_lists)

    return answer

print(solution([7,9,1,1,4]))