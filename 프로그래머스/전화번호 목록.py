def solution(phone_book):
    # 1. Hash map을 만든다
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    # 2. 접두어가 Hash map에 존재하는지 찾는다
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True
# ---------------------------------------------------------------
# def solution(phone_book):
    
#     for i in range(len(phone_book)): # 한놈씩 뽑아서 조사
#         a = phone_book.pop(i) 
#         b = len(a) 
#         for j in range(len(phone_book)):
#             if phone_book[j][:b] == a:
#                 return False
#         # 뺀거 추가해주기
#         phone_book.insert(i,a)
        
#     return True

# 해쉬풀이 ---------------------------------------------------------------------------------------

def solution(phone_book):
    
    # 1. Hash map을 만든다
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for i in phone_book: # 한놈씩 뽑아서 조사
        # 해쉬맵 돌면서 조사
        for key in hash_map.keys():
            if i != key and key[:len(i)] == i:
                return False
        
        
    return True