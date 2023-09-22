def solution(want, number, discount):
    answer = 0

    # 슬라이싱과 딕셔너리 이용해서 해보자

    # 딕셔너리에 want와 개수 넣기
    dic1 = {}
    
    for i,j in zip(want,number):
        dic1[i] = j

    # discount 조사
    for k in range(len(discount)-10+1):
        list = discount[k:k+10]
        dic2 = {}
        # 밑에는 슬라이싱으로 자른거 딕셔너리로 넣기
        for z in list:
            if z in dic2:
                dic2[z] += 1
            else:
                dic2[z] = 1

        if dic1 == dic2:
            answer += 1

    return answer



want = ["apple"]
number = [10]
discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
print(solution(want,number,discount))