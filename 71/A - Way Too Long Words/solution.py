num = int(input())
 
for i in range(num):
    word = list(input())
 
    if len(word) <= 10:
        print(''.join(map(str, word))) 
    else:
        print(word[0] + str(len(word) - 2) + word[-1])