def solution(storey):
    answer= []
    # dfs로 풀어볼예정
    # 아이디어: 한자리씩 체크해봐서 up 인지 down인지 보고 5일때는 두군데 다 가보기
    def dfs(st,cnt):

        if st == 0:
            answer.append(cnt)
            return answer
        
        one = st % 10
        up, down = 10-one,one

        if up < down:
            dfs(st//10 + 1,cnt + up) # up해서 한자리 올라갔으니까
        if up > down:
            dfs(st//10 ,cnt + down)
        if up == down: # 위로도 가보고 아래로도 가보기
            for i in range(2):
                dfs(st//10 + i,cnt + up)
    
    dfs(storey,0)
    return min(answer) # 두방향 모두 쌍이겠지 answer에 그 중 최소 뽑기


# 테스트
print(solution(16))  # 출력: 6
print(solution(2554))  # 출력: 16
