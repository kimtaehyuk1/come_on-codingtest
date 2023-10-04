def solution(numbers):
    str_numbers = [str(num) for num in numbers] # 일단 문자열은 앞에서부터 비교하니까 즉 4 가 30보다 큰거다
    str_numbers.sort(key= lambda i : i*3, reverse=True) # i*3을 하는 이유는 만약 3 331 있는데 더 크려면 3331이 난데 만약 *2만 해주면  33과 331331 이어서 다 비교 안된다 즉 *3해서 1000전까지 채우주기
    # 조합만 하면 끝
    answer = str(int(''.join(str_numbers))) #000있으면 0하고 다시 str이니까
    return answer