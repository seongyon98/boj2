N = int(input())

ps = [(200, 209, 8), (200, 219, 4), (200, 229, 2), (200, 239, 1)]

lvl = -1
idx = -1
for i, (s, e, c) in enumerate(ps):
    l = N
    for _ in range(c):
        if s <= l <= e:
            l += 1
        else:
            break
    if l > lvl or (l == lvl and i > idx):
        lvl = l
        idx = i

print(idx + 1)