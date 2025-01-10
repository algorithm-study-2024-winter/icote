# 1일 될 때까지

n, k = list(map(int, input().split()))

ret = 0
while n != 1:
  a1 = n-1
  a2 = n % k
  
  if a2 == 0:
    n= min(a1, n/k)
  else:
    n = a1
  ret += 1
  
print(ret)