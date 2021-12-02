# Project Euler Problem 2 - Even Fibonacci numbers
# https://projecteuler.net/problem=2

a, b = 1, 1
ans = 0
while b < 4000000:
    if b % 2 == 0:
        ans += b
    a, b = b, a + b

print(ans)

