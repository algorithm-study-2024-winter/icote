# 1026 보물
# https://www.acmicpc.net/problem/1026

n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

bl.sort()
al.sort(reverse=True)

ret = 0
for a, b in zip(al, bl):
  ret += a * b
  
print(ret)