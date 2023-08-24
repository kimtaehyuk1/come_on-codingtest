clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

cnt = 1 #한개씩 입는거 세는거

# 첫번째로 hash_map 만들어서 key 값 짚어넣기
hash_map = {}
for cloth in clothes:
    value, key = cloth
    if key in hash_map:
        hash_map[key].append(value)
    else:
        hash_map[key] = [value]

# 전략: 아예 안입은 경우도 추가해서 곱한후 -1(모두 안입는 경우 빼기)
for i in hash_map:
    cnt *= (len(hash_map[i]) + 1)

print(cnt-1)
    


