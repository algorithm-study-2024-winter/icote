# 회의실 배정
# https://www.acmicpc.net/problem/1931

# 시작시간, 끝나는 시간 -> 회의 최대 개수

n = int(input())

convs = []
for _ in range(n):
  a, b = map(int, input().split())
  convs.append([a, b])

convs.sort(key=lambda x: (x[1], x[0]))
ret = []
for i in convs:
  if not ret:
    ret.append(i)
  else:
    if i[0] >= ret[-1][1]:
      ret.append(i)

print(len(ret))