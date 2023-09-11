def solution(park, routes):
    # 북 동 남 서
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    # 유효범위 함수
    def is_valid(y, x):
        return 0 <= y < len(park) and 0 <= x < len(park[0])

    # 공원의 가로 세로 길이 받기
    H = len(park)  # 세로 길이
    W = len(park[0])  # 가로 길이

    # 어디서 S인지 받기
    for i, v in enumerate(park):
        for j, k in enumerate(v):
            if k == 'S':
                start = [i, j]
                break

    # 동서남북 매칭하기(routes) -> 여기가 메인 동작
    for i in routes:
        dir, dis = i.split()
        dis = int(dis)
        # 동쪽일 때
        if dir == 'E':
            back = start #어디서 들어오든 start바뀌있어도 그 바뀐값으로 밑에서 시작하면 되니까
            for _ in range(dis):  # dis만큼 반복
                tmp = [start[0], start[1] + dx[1]]
                if not is_valid(tmp[0], tmp[1]) or park[tmp[0]][tmp[1]] == 'X':
                    # 여기서 안될을시 처음으로 돌아가는 코드
                    start = back
                    break
                else: # 이걸해줘야 계속해서 업뎃
                    start = tmp

        elif dir == 'W':
            back = start
            for _ in range(dis):  # dis만큼 반복
                tmp = [start[0], start[1] + dx[3]]
                if not is_valid(tmp[0], tmp[1]) or park[tmp[0]][tmp[1]] == 'X':
                    start = back
                    break
                else:
                    start = tmp

        elif dir == 'S':
            back = start
            for _ in range(dis):  # dis만큼 반복
                tmp = [start[0] + dy[2], start[1]]
                if not is_valid(tmp[0], tmp[1]) or park[tmp[0]][tmp[1]] == 'X':
                    start = back 
                    break
                else:
                    start = tmp

        elif dir == 'N':
            back = start
            for _ in range(dis):  # dis만큼 반복
                tmp = [start[0] + dy[0], start[1]]
                if not is_valid(tmp[0], tmp[1]) or park[tmp[0]][tmp[1]] == 'X':
                    start = back
                    break
                else:
                    start = tmp
        
    return start

park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]

print(solution(park, routes))
