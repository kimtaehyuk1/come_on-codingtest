# 백준 1302 문제

# 딕셔너리 문제
d = dict()

for _ in range(int(input())):
    book = input()
    # 입력book이 있으면 +1 아니면 처음 한권이다
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

# 최대로 많이 팔린 놈의 갯수알기
m = max(d.values())
# m의 수와 같은 책들 리스트에 담기(오름차순해서 맨앞에꺼 뽑기위해)
candi = []
for k , v in d.items():
    if v == m:
        candi.append(k)

# 담겨진 candi에서 sort후 젤 앞에꺼 뽀기
candi.sort()
print(candi[0])
