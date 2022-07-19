import sys
import copy
input = sys.stdin.readline

cN = int(input())
cL = list(map(int, input().split()))
bN = int(input())
bL = list(map(int, input().split()))

cL.sort(reverse=True)
bL.sort(reverse=True)

if(cL[0] < bL[0]): # 불가능하면 -1 출력하고 출력
    print(-1)
    sys.exit()
    
ans = 0
box_to_move = copy.deepcopy(bL)

while(box_to_move): # 무조건 가능
    check = False
    for c in cL:
        for b in box_to_move:
            if c >= b: # 옮길 수 있는 경우
                box_to_move.remove(b)
                if(c == cL[len(cL) - 1]): # 모든 크레인이 작동하여 옮긴 경우
                    ans += 1
                    check = True
                elif(not box_to_move): # 모든 크레인이 작동하지는 않았지만 옮길 박스가 없는 경우
                    ans += 1
                    check = True
                break
            elif b == box_to_move[len(box_to_move) - 1]: # 어느 크레인에서, 옮겨야 하는 마지막 박스까지 확인했는데 못 옮긴 경우
                ans += 1
                check = True # 뒤에 크레인들은 볼 것도 없음
                break
        if check == True: # 뒤에 크레인들은 볼 것도 없음
            break
                        
print(ans)