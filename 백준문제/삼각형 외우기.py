# 백준 10101 삼각형 외우기 문제

# for i in range(3):
#     for j in input():
#         print(j)

s = []

for i in range(3):
    s.append(int(input()))


if sum(s) == 180:
    # 180면 일로 들어와서 첫번째로 세각 다 같은거 판별하기 위해 집합쓰기 어짜피 50 50 50 은 여기 들어오지도 못하니까 이거 허용됨
    if len(set(s)) == 1:
        print('Equilateral')
    elif len(set(s)) == 2:
        print('Isosceles')
    else:
        print('Scalene')

else:
    print('Error')