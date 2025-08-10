t = int(input())

fst = [(1, 500), (2, 300), (3, 200), (4, 50), (5, 30), (6, 10)]
snd = [(1, 512), (2, 256), (4, 128), (8, 64), (16, 32)]


def pz(rnk, y):
    if rnk == 0:
        return 0
    for cnt, p in y:
        if rnk <= cnt:
            return p
        rnk -= cnt
    return 0


for _ in range(t):
    a, b = map(int, input().split())
    total = pz(a, fst) + pz(b, snd)
    print(total * 10000)
