# 규칙: 우선 노란색으로 해결할 생각 (노란색가로*2)+(노란색세로*2) +4 가 brown개수이고,
# [노란색가로+2,노란색세로+2]가 답이다
# 노란색 가로 세로 구하기 위해 주어진 yellow에서 약수 * 약수 로 해서 brown 개수 만족하면 그수의 [노란색가로+2,노란색세로+2] 답이다

def solution(brown, yellow):
    answer = []
    yellow_x = 0 #노란색가로
    yellow_y = 0 #노란색세로
    
    # 약수 찾기
    for i in range(1,yellow+1):
        if yellow % i == 0:
            # 약수끼리 곱해서 yellow가 되야됨.
            yellow_x = yellow // i
            yellow_y = i
            if (yellow_x*2)+(yellow_y*2)+4 == brown:
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                
                return answer
    
    return answer