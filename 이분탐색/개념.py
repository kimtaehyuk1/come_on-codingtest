# 이진탐색은 탐색 전에 반드시 정렬되어 있어야 한다!
# 이진탐색 = 정렬 O(NlogN) + 이진탐색 O(logN) = NlogN이다, 선형탐색은 N인데 그럼 선형이 더 좋은거 아니냐?
# 만약 한개만을 찾는거라면 선형탐색이 좋은데, N개 찾는거라면 선형은 N제곱이고 이분은 NlogN(정렬) + NlogN이니까 이게 이득이다. 

from bisect import bisect_left, bisect_right
v = (0,1,3,3,6,6,6,7,8,8,9)
three = bisect_right(v,3) - bisect_left(v,3) # 이렇게 하면 3의 개수가 나옴

# 파라메트릭 서치 : 최적화 문제(변수의 최솟값, 최댓값을 구하는 문제) 를 결정 문제(Yes/No 문제)로 바꿔서 이진탐색으로 푸는 방법이다.