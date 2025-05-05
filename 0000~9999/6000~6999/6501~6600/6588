import sys
input = sys.stdin.readline

MAX_N = 1000000

is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX_N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

primes = [i for i in range(3, MAX_N + 1, 2) if is_prime[i]]
prime_set = set(primes)

while True:
    n = int(input())
    if n == 0:
        break

    found = False
    for a in primes:
        if a > n // 2:
            break
        b = n - a
        if b in prime_set:
            print(f"{n} = {a} + {b}")
            found = True
            break

    if not found:
        print("Goldbach's conjecture is wrong.")