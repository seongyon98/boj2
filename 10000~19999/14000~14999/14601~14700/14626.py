isbn = input().strip()

w = [1, 3] * 6
t = 0
m = -1

for i in range(12):
    if isbn[i] == "*":
        m = i
        continue
    t += int(isbn[i]) * w[i]

c = int(isbn[12])

for x in range(10):
    s = t + x * w[m]
    if (s + c) % 10 == 0:
        print(x)
        break
