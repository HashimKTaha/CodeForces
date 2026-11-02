num = int(input())
color = input()
color_list = list(color)
 
x = 0
 
for i in range(num -1 ):
    if color_list[i] == color_list[i +1 ]:
        x = x +1 
 
 
print(x)
 