ts, bs = [], []
for _ in range(int(input())):
    T, B = map(int, input().split())
    ts.append(T)
    bs.append(B)

print((max(ts) * min(bs)) % 7 + 1)