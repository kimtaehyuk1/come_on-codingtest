# 이러한 기법(다시 풀어보기)
def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while bridge:
        
        answer += 1
        bridge.pop(0)
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:            
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
                 
         
    return answer














# from collections import deque

# bridge_length = 100
# weight = 100
# truck_weights = [10]

# dq = deque(truck_weights)

# # 건너고 있는 트럭 리스트(여기서 무조건 bridge_length 넣는데 만약 weight넘으면 못넘고, 넣고 빼고 할땐 cnt +1 해주기)
# way_list = deque([]) # 다리 건너는 트럭
# pass_list = deque([])#다리를 지난 트럭
# time = 0

# while True:
#     a = dq.popleft()
#     # 마지막 dq에 없는거 뺄라했을때 처리 필요
#     if len(dq) == 0:
#         # way에 있는거 그대로 pass로 옮겨주기
#         # 과정상 여기서 뺀 a 넣어주기
#         way_list.append(a)
#         time += 1
#         for i in range(len(way_list)):  
#             c = way_list.popleft()
#             pass_list.append(c)
#             time += 1
#         break

#     if len(way_list) <= bridge_length and (sum(way_list)+a) <= weight:
#         way_list.append(a)
#         time += 1
#     else:
#         b = way_list.popleft()
#         time += 1
#         pass_list.append(b)
#         # 뺸거 넣고 time 추가
#         way_list.append(a)
#         time += 1

# print(time)
