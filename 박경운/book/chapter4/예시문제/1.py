# 상하좌우

n = int(input())
di = list(input().split())

cur = [0, 0]
for i in di:
  if i == "R":
    if cur[1]+1 >= n:
      continue
    cur[1] += 1
  elif i == "L":
    if cur[1]-1 < 0:
        continue
    cur[1] -= 1
  elif i == "U":
    if cur[0]-1 < 0:
      continue
    cur[0] -= 1
  elif i == "D":
    if cur[0] + 1 >= n:
      continue
    cur[0] += 1

print(f"{cur[0]+1} {cur[1]+1}")