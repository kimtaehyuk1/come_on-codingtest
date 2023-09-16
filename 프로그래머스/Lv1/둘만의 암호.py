
# def solution(s, skip, index):
#     answer = []

#     for i in s:
#         # 만약 skip에 들어가는 알파벳있으면 그 숫자만큼 더해줘서 + index하면 된다.
#         # 일단 +index만큼 리스트에 담기
#         tmp = []
#         for j in range(index):
#             tmp.append(chr(ord(i)+(j+1)))
        
#         skip_count = 0  # sum 위치도 여기가 적합
#         # tmp 리스트에서 skip 문자열에 포함된 문자 개수 세기
#         for k in tmp:
#             if k in skip:
#                 skip_count += 1

#         # z가 넘어가는경우 처리하기
#         real = ord(i)+index+skip_count #최종 알파벳을 ord로 나타낸거


#         if real > ord('z'):
#             remain = real - ord('z')
#             answer.append(chr(ord('a')+(remain-1)))
#         else:
#             answer.append(chr(ord(i)+index+skip_count))
    
#     answer = ''.join(answer)

#     return answer


s = "aukks"
skip = "wbqd"
index = 5

def solution(s,skip,index):
    answer = ''

    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for ch in skip:
        if ch in alpha:
            alpha = alpha.replace(ch, "")

    for i in s:
        change = alpha[(alpha.index(i)+index)%len(alpha)] #여기 중요!
        answer += change

    return answer

print(solution(s,skip,index))