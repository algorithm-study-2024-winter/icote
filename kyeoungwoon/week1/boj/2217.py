# 로프
# https://www.acmicpc.net/problem/2217

n = int(input())

ropes = []
for _ in range(n):
  ropes.append(int(input()))

ropes.sort(reverse=True)

m = 0
for idx, w in enumerate(ropes):
  m = max(m, w*(idx+1))
  
print(m)