'''
문제 url : https://www.notion.so/2db33e20a79a4d46b87549cddafa6038?pvs=4#4fea3691d5ea4e758e8c3d623ef6fe3b
'''

"""
문제해결방법  -> 거꾸로 생각
5000
2500
1250
625  안나눠지면 n -1 하고 answer는 +1
624 
312
156
78
39  n -1 , anw += 1
38  
19  n -1 , anw += 1
18 
9   n -1 , anw += 1
8 
4
2
1 n -1 , anw += 1


방법 n % 2 == 0 -> n // 2, n % 2 != 0 -> ans += 1 n -= 1

"""

def solution(n):
    answer = 0
    
    while n > 0:

        if n % 2 == 0:
            n = n // 2
        else:
            answer += 1
            n -= 1

    return print(answer)

solution(5000)