# 백준 1213문제 팰린드롬 만들기
# 팰린드롬을 만드려면 알파벳 한종류까지는 홀수로 있어도되고, 나머지는 모두 짝수여야한다.

c = dict() # 'A' : 2  알파벳 종류와 몇개 사용됬는지
s = input()
for ch in s:
    if ch in c:
        c[ch] += 1
    else:
        c[ch] = 1


# c = dict() # 'A' : 2  알파벳 종류와 몇개 사용됬는지
# s = input()
# for ch in s:
#     if ch in c:
#         c[ch] += 1
#     else:
#         c[ch] = 1
# 위의 것을 대신하는게 from collections import Counter
# c = Counter(input() 이 딕셔너리에 담아준느 부분을 대신 해준다



# 한번에 바로 할랑게 집중
# 문자가 홀수인지 짝수인지 검사 그리고 홀수개가 1개 초과면, 미안출력
if sum(i % 2 for i in c.values()) > 1: # 여기서 3 이나오면 홀수가 3개 있다는거
    print("I'm Sorry Hansoo") # 팰림드롬 안되는거
else: # 팰린드롬 만들기
    half = ''
    for k,v in sorted(c.items()):
        half += k * (v // 2)

    ans = half
    # 홀수 있으면 중간에 낑기기
    for k,v in c.items():
        if v % 2: #만약 홀수면
            ans += k
            break

    ans += ''.join(reversed(half))

    print(ans)