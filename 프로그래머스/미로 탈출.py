from collections import deque 
#   북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


# 아이디어: 레버까지 bfs가고 레버에서 EXIT까지 bfs로 간다.


def solution(maps):
    
    # 유효범위 체크하기
    def is_valid(y,x):
        return 0<=y<len(maps) and 0<=x<len(maps[0])

    
    def bfs(start,target): # bfs두번 쓸거니까 고정 체크배열 ㄴ
        # 체크셋 만들기
        chk = set()
        # 체크배열에 시작점 표시하기(bfs 거기서 시작이니까)
        chk.add(start)
        # bfs에서 쓸 큐 만들기
        dq = deque()
        # 시작위치와 카운트를 셀 항목 넣기
        dq.append((start,0))

        while dq:
            (y, x), d = dq.popleft() # 시작과 셀 변수 빼기
            
            # 만약 타겟을 만나면 갯수 return
            if (y,x) == target:
                return d
            
            nd = d + 1
            # 4방향 탐색
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if is_valid(ny,nx) and (ny,nx) not in chk and maps[ny][nx] != 'X': # maps[ny][nx] != 'X'이거여야 레버와 exit도 가는거
                    chk.add((ny,nx))
                    dq.append(((ny,nx),nd))
                    
        return -1 # dq가 없을때
        
    start, lever, exit = None, None, None    
    # 들어온 maps에서 스타트,레버,엑시트 위치 파악하기
    for i,v in enumerate(maps):
        for j,k in enumerate(v):
            if k == 'S':
                start = (i,j)
            if k == 'L':
                lever = (i,j)
            if k == 'E':
                exit = (i,j)    
                
    start_to_lever = bfs(start,lever)
    lever_to_exit = bfs(lever,exit)
    
    if start_to_lever== -1 or lever_to_exit==-1:
        return -1
    
    return start_to_lever + lever_to_exit