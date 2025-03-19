import random
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 2
    if n > 2:
        factors.add(n)
    return factors

def find_primitive_root(p):
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)):
            return g
    return None

p = int(input("Enter a prime number (p): "))
if not is_prime(p):
    print("p must be a prime number.")
    exit()

g = find_primitive_root(p)
if g is None:
    print("No primitive root found for p.")
    exit()

    
a = random.randint(1, p - 1)
b = random.randint(1, p - 1)  

A = pow(g, a, p)  
B = pow(g, b, p)

shared_secret_A = pow(B, a, p)  
shared_secret_B = pow(A, b, p) 

print(f"Primitive root (g): {g}")
print(f"Alice's private key (a): {a}")
print(f"Bob's private key (b): {b}")
print(f"Alice's public key (A): {A}")
print(f"Bob's public key (B): {B}")
print(f"Shared secret (Alice): {shared_secret_A}")
print(f"Shared secret (Bob): {shared_secret_B}")