import math
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

p=int(input("Enter p:"))
q=int(input("Enter q:"))

if not (prime(p) and prime(q) and p != q):
    print("Numbers are not prime numbers .")
    exit()

msg = int(input("Enter message (integer)- "))

n=p * q
phi=(p - 1) * (q - 1)

while True:
    e = int(input(f"Enter a public exponent 'e' (1 < e < {phi}, coprime with {phi}): "))
    if 1 < e < phi and math.gcd(e,phi) == 1:
        break
    print("Invalid e.")

d = pow(e, -1, phi)

C = pow(msg, e, n)  
M = pow(C, d, n)

print(f"Encrypted: {C}\nDecrypted: {M}")