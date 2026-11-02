inp = input()
unq = set(inp)
char = len(unq)
 
if char % 2 == 0:
    print("CHAT WITH HER!")
elif char % 2 != 0:
    print("IGNORE HIM!")
    