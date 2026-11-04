inp = input()
n = 0
 
for i in range(len(inp)):
    if inp[i] == '4' or inp[i] == '7':
        n += 1
        continue
if n == 4 or n == 7:
    print("YES")
else:
    print("NO")