games = int(input())
win = input()
a = 0
d = 0
 
for i in range(games):
    if win[i] == 'A':
        a += 1
    elif win[i] == 'D':
        d += 1
if d == a:
    print("Friendship")
elif d >= a:
    print("Danik")
else:
    print("Anton")
 