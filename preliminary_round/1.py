# F를 사용한 코드
# 거의 모두 완벽하게 작동
m, f, n = map(int,input().split())
tmp = n-f+1
res = 0

if f == 1:
  res = 0
else:
  res = 1
  tmp -= min(tmp%(m-1), (m-f))

if tmp//(m-1) == 0:
  if tmp%(m-1) != 0:
    res += 1
else:
  res += tmp//(m-1)
  if tmp%(m-1) != 0:
    res += 1

print(res)

# F를 사용하지 않은 코드 
# 작동을 하긴 하지만 문제가 있을 수 있음
'''
M, F, N = map(int, input().split()) #배찌가 살고 있는 건물의 층수 / 배찌가 사는 층수 / 배찌가 오르고 싶은 계단의 총 층수

elv = 1 #엘리베이터를 탄 횟수의 기본 값을 1로 한다. (처음에 1층으로 가야하기 때문)

elv = elv + N // M #배찌가 오르고 싶은 계단의 총 층수와 배찌가 살고 있는 건물의 층수를 나눠 나온 몫을 더한다.

print(elv) #여기서 구하는건 베찌가 엘리베이터를 얼마나 탔는지 이므로 엘리베이터를 탄 횟수를 출력한다.
'''