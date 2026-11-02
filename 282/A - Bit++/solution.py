n = int(input())
x = 0
 
for i in range(n):
    num = list(input())
 
    for y in range(len(num)):
            if num[1] == "+":
                x = x + 1
                break
     
            elif num[1] == "-":
                x = x - 1
                break
 
print(x)
 
 