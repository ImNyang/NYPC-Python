# 입력 예제 1이 작동하지 않습니다.

#output : 11

num_many = int(input()) # 이 배열의 크기를 나타내는 입력을 받는다.
tmp_list = input().split() # 리스트를 입력받습니다.
num_of_list = list(map(int, tmp_list)) # 리스트로 만듭니다.

sum_tmp = 0 # tmp의 모드 더한값 받기
sum_res = 0 # res의 모두 더한값을 받을 함수 

def deQuote(list):
    for i in range(0, len(list)):
        list[i] = int(list[i])

def findMaxSpan(list, k):
    size = len(list)                                        # 목록의 길이
    max = list[0]                                           # 임시 최대 구간합

    for start in range(0, size - k + 1):                    # strat = 구간 출발 위치
        sum = list[start]                                   # 현재 구간 합 초기화

        for i in range(1, k):                               # 현재 구간 내 원소들
            sum += list[start +i]                           # 원소 합산

        if sum > max:                                       # 최대 구간합 갱신
            max = sum

    return max

deQuote(num_of_list)

max = findMaxSpan(num_of_list, num_many)
print(max)



