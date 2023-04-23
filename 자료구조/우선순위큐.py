# 우선순위 큐(Heap=이진트리)
# 트리에서 root노드가 젤 큰값이면 max-heap, 젤 작으면 min-heap
# 파이썬에서 루트노드에 젤 작은값이 위치


# from queue import PriorityQueue

# pq = PriorityQueue()
# pq.put(6)
# pq.put(10)
# pq.put(-5)
# pq.put(0)
# pq.put(8)

# while not pq.empty():
#     print(pq.get()) # pop역활

# 출력값이 밑에처럼 나온다 PriorityQueue()는 루트노드에 젤 작은게 올라와서 빠질때 작은거 순으로 빠짐
# -5
# 0
# 6
# 8
# 10

# 위에도 느리기 때문에 heapq라는것을 쓴다.
import heapq

pq = []
heapq.heappush(pq, 6)
heapq.heappush(pq, 12)
heapq.heappush(pq, 0)
heapq.heappush(pq, -5)
heapq.heappush(pq, 8)
print(pq) # [-5, 0, 6, 12, 8] 
while pq:
    print(pq[0])
    heapq.heappop(pq)

# 돌려보면 결과가 작은거 순으로 빠져나온다
# -5
# 0 
# 6 
# 8
# 12