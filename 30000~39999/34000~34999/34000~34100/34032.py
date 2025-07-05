int(input())
gg = input()

o, x = 0, 0
for c in gg:
    if c == "O":
        o += 1
    else:
        x += 1

print("Yes" if o >= x else "No")