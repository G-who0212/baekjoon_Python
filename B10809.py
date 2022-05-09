alpha = [-1]*26
word = input()
for i in range(len(word)):
    if alpha[ord(word[i])-97] != -1:
        continue
    else:
        alpha[ord(word[i]) - 97] = i
        
for i in range(26):
    print(alpha[i], end=' ')