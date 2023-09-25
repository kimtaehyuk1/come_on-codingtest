# 문제 url : https://school.programmers.co.kr/learn/courses/30/lessons/131701


def solution(elements):
    
    answer = 0
    # 연속된거니까 배열 받은걸 두배해서 붙이자
    dou_elements = elements * 2
    # 길이가 1부터 길이가 len(elements)까지 할껀데 길이 1하고, len(elements)는 정해저 있으니까 for를 그 사이만 돌고 더해주자
    

    cnt_lsit = []  #더할거 담아줄 그릇

    # 사이값 돌려주기
    for i in range(1,len(elements)+1): # 길이 for문
        for j in range(len(elements)): #여긴 실제 돌릴for문 인덱스로
            tmp = sum(dou_elements[j:j+i])
            cnt_lsit.append(tmp)

    #여기서 일관적으로 set처리
    cnt_set = set(cnt_lsit)

    answer = len(cnt_set)

    return answer


elements = [7,9,1,1,4]
print(solution(elements))



# def solution(elements):

#     answer = 0
#     init_len = len(elements)

#     # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
#     elements = elements * 2
#     result_lists = set()

#     def part_fib_sum2(m):
#         for i in range(init_len):
#             result_lists.add(sum(elements[i:i+m]))

#     for i in range(1, init_len+1):
#         part_fib_sum2(i)

#     answer = len(result_lists)

#     return answer

# print(solution([7,9,1,1,4]))