M, F, N = map(int, input().split()) #배찌가 살고 있는 건물의 층수 / 배찌가 사는 층수 / 배찌가 오르고 싶은 계단의 총 층수

elv = 1 #엘리베이터를 탄 횟수의 기본 값을 1로 한다. (처음에 1층으로 가야하기 때문)

elv = elv + N // M #배찌가 오르고 싶은 계단의 총 층수와 배찌가 살고 있는 건물의 층수를 나눠 나온 몫을 더한다.

print(elv) #여기서 구하는건 베찌가 엘리베이터를 얼마나 탔는지 이므로 엘리베이터를 탄 횟수를 출력한다.