keymap = ["AA"]
targets = 	["B"]
answer = []


hash_map = {}

for i in keymap:
    tmp = 1 #이 위치가 적당
    for j in i:
        # 애초에 여기서 월래 있는 tmp랑 새로오는 tmp비교해서 작은걸로 세팅
        # 해쉬 맵에 없을때
        if j not in hash_map:
            hash_map[j] = tmp
        else: # 해쉬맵에 있을때
            if hash_map[j] > tmp:
                hash_map[j] = tmp # 현재 들어온 작은 tmp와 바꾸기
        tmp += 1
    
# 해쉬맵 채웠으니 타겟 조지기
for i in targets:
    anscnt = 0
    for j in i:
        if j in hash_map:
            anscnt += hash_map[j]
        else:
            anscnt = -1
            break # 안되는거 만나면 바로 멈춰야지 아니면 -1 에 계속 더해진다.
    answer.append(anscnt)

print(answer)
