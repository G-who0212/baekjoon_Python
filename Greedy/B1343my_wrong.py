import sys

def input():
    return sys.stdin.readline().rstrip()

inp = input()
A = [] # 'X'
B = [] # '.'
x = 1
if(len(inp) == 1):
    if(inp[0] == 'X'):
        A.append(1)
    else:
        B.append(1)
for i in range(1, len(inp)):
    if(i == len(inp)-1):
        if(inp[i] == 'X'):
            A.append(x + 1)
        else:
            B.append(x + 1)
    if(inp[i-1] != inp[i]):
        if(inp[i-1] == 'X'):
            A.append(x)
            x = 1
        else:
            B.append(x)
            x = 1
    else:
        x += 1
# print(A)
# print(B)
odd = 0
for i in range(len(A)):
    if(A[i] % 2 == 1):
        odd = 1
        break
        
if(odd == 1): print(-1)      
else:
    if(inp[0] == 'X'): # 첫 시작이 'X'일 때
        for i in range(len(A)):
            if(A[i] % 2 == 1):
                print(-1)
                break
            elif(A[i] % 4 != 0):
                for _ in range(A[i] // 4):
                    print("AAAA", end='')
                print("BB", end='')
            else:
                for _ in range(A[i] // 4):
                    print("AAAA", end='')
            if(i != len(B)):
                for _ in range(B[i]):
                    print('.', end='')
    else:
        for i in range(len(B)):
            for _ in range(B[i]):
                print('.', end='')
            if(i != len(A)):
                if(A[i] % 2 == 1):
                    print(-1)
                    break
                elif(A[i] % 4 != 0):
                    for _ in range(A[i] // 4):
                        print("AAAA", end='')
                    print("BB", end='')    
                else:
                    for _ in range(A[i] // 4):
                        print("AAAA", end='')