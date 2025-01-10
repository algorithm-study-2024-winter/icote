# 큰 수의 법칙

n, m, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()

ret = 0
repeat = 0
for _ in range(m):
  if (repeat < k):
    ret += nums[-1]
    repeat += 1
  else:
    ret += nums[-2]
    repeat = 0

print(ret)

'''
반복적으로 진행되므로, 반복되는 수열의 길이를 나누어 계산하기 가능 ..
'''