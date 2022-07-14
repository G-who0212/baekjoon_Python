import sys

def input():
    return sys.stdin.readline().rstrip()

board = input().replace('XXXX', 'AAAA').replace('XX', 'BB')

# if 'X' in board:
#     print(-1)
# else:
#     print(board)
    
print(board if 'X' not in board else -1)