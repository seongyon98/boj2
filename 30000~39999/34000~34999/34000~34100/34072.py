levels = []
for _ in range(int(input())):
    levels.append(int(input()))
    
if levels[0] == min(levels):
    print("ez")
elif levels[0] == max(levels):
    print("hard")
else:
    print("?")