n, m = map(int, input().split())
check_set = [[0,0]]*(n+1)
for j in range(m):
  t, i, state = map(int, input().split())
  if state == 0:
    if check_set[i][1] == 1:
      print("NO")
    check_set[i] = [t, 1]
      
  else:
    if check_set[i][1] == 0:
      print("NO")
    elif t-check_set[i][0] < 60:
      print("NO")
    else:
      check_set[i] = [0,0]
for k in range(1, n+1):
  if check_set[k][1]==1:
    print("NO")
print("YES")