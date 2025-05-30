ans = -1
for _ in range(int(input())):
    A, B, C = map(int, input().split())
    t = A + B + C
    if t >= 512 and (ans == -1 or t < ans):
        ans = t

print(ans)