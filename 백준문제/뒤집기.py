# 백준 10816문제
import sys
intput = sys.stdin.readline

# 리스트로 만들어서 1뒤집을때랑 0뒤집을때랑 두개 비교후 작은거 ans출력
S = list(input())
cnt = 0

# 입력값에서 숫자 바뀌는거 조사해서 //2 하면 답이다
for i in range(len(S)-1):  # len(S)-1이렇게 해야 i 와 i+1 조사할거기 때문에
    if S[i] != S[i+1]:
        cnt += 1

print( (cnt+1) // 2)




