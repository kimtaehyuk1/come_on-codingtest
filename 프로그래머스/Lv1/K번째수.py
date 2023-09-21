def solution(array, commands):
    answer = []

    for i in commands:
        select_array = array[i[0]-1:i[1]]
        # 선택받은 array정렬하기
        select_array.sort()
        # 정렬 후 k번째 숫자 뽑기
        answer.append(select_array[i[2]-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array,commands))