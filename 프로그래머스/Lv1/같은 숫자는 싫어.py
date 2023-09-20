def solution(arr):

    # 스택만들기
    stk = []

    for i in arr:
        if stk:
            # 스택에 있는거랑 지금 들어오는거 비교해서 같으면 넣지 않기
            if stk[-1] != i:
                stk.append(i)
        else:
            stk.append(i)

    
    return stk


arr = [4,4,4,3,3]
print(solution(arr))