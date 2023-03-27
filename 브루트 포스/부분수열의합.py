# 문제 url : https://www.acmicpc.net/problem/1182

# 문제 이해는 사진 참고
# 조합문제임
# 다 찾아서 무식하게 하는 브루트 포스 방식


from itertools import combinations
# 입력
N, S = map(int,input().split())
A = list(map(int, input().split()))

ans = 0
for num_elements in range(1,N + 1):  # 몇개의 조합을 찾을건지 물고 들어가기
    for c in list(combinations(A, num_elements)): #combinations(A, num_elements)는 받은A에서 num_elements수의 조합을 모두 찾는다.
        if sum(c) == S:
            ans += 1

print(ans)