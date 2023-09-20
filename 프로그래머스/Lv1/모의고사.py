def solution(answers):
    answer = []
    
    one = [1,2,3,4,5] * 2000
    two = [2,1,2,3,2,4,2,5] * 1250
    three = [3,3,1,1,2,2,4,4,5,5] * 1000

    # 리스트들 큰 리스트에 담기
    big_list = [one,two,three]

    # 각자 찍는 방법으로 맞는 숫자세서 비교하는 딕셔너리 만들기
    cnt_dic = {}

    # zip함수로 풀어보자
    for index,i in enumerate(big_list):
        cnt = 0
        for j,k in zip(i,answers):
            if j == k:
                cnt += 1
        # key-value로 정답 맞춘개수 넣기
        cnt_dic[f"list_{index+1}"] = cnt  

    # 가장 cnt가 높은거
    h_cnt = max(cnt_dic.values())

    for a,b in cnt_dic.items():
        if b == h_cnt:
            answer.append(a) # 가장큰 cnt를 가지는 놈의 key값을 앤써에 넣기
    

    # 영어로 되어있는거 숫자로 바꿔주기
    string_to_number = {'list_1':1,'list_2':2,'list_3':3}

    answer = [string_to_number[s] for s in answer]


    # 만약에 cnt 들어있는거 2개이상이면 오름차순 정리하기
    answer.sort()

    return answer

answers = [1,3,2,4,2]
print(solution(answers))