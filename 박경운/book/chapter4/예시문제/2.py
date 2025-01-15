# 시각

n = int(input())

ret = 0
for h in range(n+1):
  for m in range(60):
    for s in range(60):
      if "3" in f"{h}{m}{s}":
        ret += 1
      
print(ret)