# 전력망을 둘로 나누기.
# 규칙발견: 배열에서 숫자가 가장 많이 나온 수 찾고 그거와 연결된 숫자중에서 타고타고 끝까지 가서 숫자 젤 높은놈꺼 끊기

def solution(n,wires):
    graph = [[] for _ in range(n+1)] # 노드 개수만큼 인덱스 그대로 쓰려고
    # 만약 n = 9라면 [[], [], [], [], [], [], [], [], [], []] 인덱스그대로 graph[1]은 1번노드에 연결되있는 다른 노드를 담기

    # 주어진 wires기반으로 graph생성
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a) #양방향

    # 재귀로 dfs돌면서 둘로 나뉘어졌을때 노드 개수세는 함수
    def dfs(node,parent):
        cnt = 1 # 무조건 나눠지고 개수세는거니까 1은 깔고 들어가야함
        for neighbor in graph[node]: #끊어진 node와 연결된거 하나씩 돌면서 세야됨으로 물론 parent와 같으면 안된다
              if neighbor != parent:
                   cnt += dfs(neighbor,node)
        return cnt
         
    answer = float('inf')
    for a, b in wires:  # 한개씩 전부 끊어보기 -> 최소값구하기
        graph[a].remove(b)
        graph[b].remove(a)

        size1 = dfs(a,b)
        size2 = n - size1

        answer = min(answer,abs(size1-size2))

        graph[a].append(b)
        graph[b].append(a)
    
    return answer



