from math import sqrt
import random
from random import randint as rand
def generate_keypair(p, q, keysize):
    nMin = 1 << (keysize - 1)
    nMax = (1 << keysize) - 1
    primes = [2]
    start = 1 << (keysize // 2 - 1)
    stop = 1 << (keysize // 2 + 1)
    if start >= stop:
        return []
    for i in range(3, stop + 1, 2):
        for p in primes:
            if i % p == 0:
                break
            else:
                primes.append(i)
    while (primes and primes[0] < start):
        del primes[0]
#choosing p and q from the generated prime numbers.
    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_values = [q for q in primes if nMin <= p * q <= nMax]
        if q_values:
            q = random.choice(q_values)
            break
    print(p,q)
    n = p * q
    phi = (p - 1) * (q - 1)
#generate public key 1<e<phi(n)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while True:
#as long as gcd(1,phi(n)) is not 1, keep generating e
        e = random.randrange(1, phi)
        g = gcd(e, phi)
#generate private key
        d = mod_inverse(e, phi)
        if g == 1 and e != d:
            break
#public key (e,n)
#private key (d,n)
    return ((e, n), (d, n),p,q)

def decrypt(msg_ciphertext, package):
    d, n = package
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
# No need to use ord() since c is now a number
# After decryption, we cast it back to character
# to be joined in a string for the final result
    return (''.join(msg_plaintext))