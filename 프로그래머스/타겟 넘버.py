def solution(numbers, target):
    
    cnt = 0 # 정답개수 세기
    # 각 수를 +1 , -1 한 결과를 모두 담을 그릇
    dish = [0] #  첫 순자에 + - 붙여줘야 함으로 0으로 시작
    # 그리고 어쩌피 밑에서 dish값을 연산 결과로 엎을거임
    
    # 모든 경우 다하는거다
    for num in numbers:
        tmp = [] # 위치 중요
        for i in dish:
            tmp.append(i-num)
            tmp.append(i+num)
        dish = tmp
    # 모든 경우의 연산 결과 담겨진 dish에서 target 개수 세기
    for j in dish:
        if j == target:
            cnt += 1
        
    
    
    return cnt