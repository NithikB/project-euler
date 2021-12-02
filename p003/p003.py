# Project Euler Problem 3 - Largest prime factor
# https://projecteuler.net/problem=3

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

n = 600851475143
for i in range(3, int(n**0.5)+1, 2):
    if n % i == 0 and isPrime(i):
        largest_prime = i

print(largest_prime)