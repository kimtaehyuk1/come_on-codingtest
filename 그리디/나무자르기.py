# 문제 url : https://www.acmicpc.net/problem/14247

# 문제 이해 ok?
# 한나무를 여러번 자르는것은 손해 ㅇㅋ? -> 왜? 다 큰거 한번에 자르나 자르고 그나무 또 자르는 길이가 같기에, 같은 나무를 두번 자르는건 손해다. 
# 즉 중복으로 나무 고르는일 없게 하기 => 모든 나무를 다 한번씩 자른다는 얘기~! => 나무를 자를 순서를 정해라는 문제로 바뀜!
# 성장속도가 큰 나무를 맨 마지막에 자르는게 이득 아닐까? -> 맞지!
# 즉 Ai 순으로 정렬해서 자르면 된다.


import sys
# 입력
N = int(sys.stdin.readline()) # 나무의 개수
H = list(map(int, sys.stdin.readline().split())) # 나무의 현재 길이
A = list(map(int, sys.stdin.readline().split())) # 나무가 하루마다 자라는 양

I = list(range(N)) # 출력 [0,1,...N-1] 나무의 개수만큼 리스트 만들어준것.


# 
I = sorted(I, key= lambda i:A[i])  #이것의 뜻은 A[i]의 값중에서 작은 순서대로 인덱스를 정렬한것!!


ans = 0
for i in range(N):
    index = I[i] # 여기서 I는 자라나는 길이가 작은 인덱스 순으로 정렬
    ans += H[index] + i * A[index]

print(ans)