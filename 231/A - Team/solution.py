n = int(input())
x = 0 
for i in range(n):
    num1, num2, num3 = map(int, input().split())
    if sum([num1, num2, num3]) <= 1:
        continue
    else:
        x = x + 1 
print(x)