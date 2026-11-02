x = int(input())
 
y = 5
z = 0
 
for i in range(x):
    if x - y > 0:
        z = z+1
        y = y+5
    else:
        z = z + 1 
        print(z)
        break
        