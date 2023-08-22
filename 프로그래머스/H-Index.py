# 문제 별루.ㅋㅋ
def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 내림차순으로 정렬
    h_index = 0
    
    for idx, citation in enumerate(citations):
        if citation >= idx + 1:
            h_index = idx + 1
            
    return h_index