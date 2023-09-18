def solution(a,b):
    # 각달의 일 수를 리스트로 저장 -> 일수로 더해서 % 7할꺼임으로
    days_in_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 2016년 1월1일 부터 요일 리스트로 담기
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    # 입력받은 총 일수 계산하기
    total = sum(days_in_list[:a-1])+b - 1 #-1은 날짜도 리스트니까 나눴을때 바로 찾아가게 하려고
    
    return days[total%7]

print(solution(5,24))