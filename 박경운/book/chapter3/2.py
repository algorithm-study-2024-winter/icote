# 숫자 카드 게임

y, x = list(map(int, input().split()))
board = []
for _ in range(y):
  ap = list(map(int, input().split()))
  board.append(min(ap))
  
print(max(board))

'''
board를 list로 쓰지 말고 primitive로 해서,
for문에서 max() 로 비교해서 넣었어도 됨.
'''