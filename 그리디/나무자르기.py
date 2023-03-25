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

I = sorted(I, key= lambda i:A[i])  #이것의 뜻은 A[i]의 값중에서 작은 순서대로 I를 정렬한 것이다. 

'''
I = [2, 0, 1]
A = [3, 1, 4]
I = sorted(I, key= lambda i:A[i])  # 이것은 I의 값이 i로 들어가서 처음에 A[2]이런식으로 값을 찾고 그 값을 기준으로 작은순대로 I를 재배열 하는것이다.
i=2일 때, A[2]=4이므로 2는 가장 큰 값입니다.
i=0일 때, A[0]=3이므로 0은 2 다음으로 큰 값입니다.
i=1일 때, A[1]=1이므로 1은 가장 작은 값입니다.
따라서 I 리스트의 원소들은 1, 0, 2 순서대로 정렬됨.
출력 : [1, 0, 2]
'''

ans = 0
for i in range(N):
    index = I[i] # 여기서 I는 자라나는 길이가 작은 순으로 정렬되 있으니까 순서대로 뽑아쓰는 느낌으로.
    ans += H[index] + i * A[index]

print(ans)