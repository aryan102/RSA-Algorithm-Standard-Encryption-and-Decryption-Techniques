from math import sqrt
import random
from random import randint as rand
from longfac import *
from chinesealgo import *
from faultkeygen import *
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1
def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True
#initial two random numbers p,q
p = rand(1, 1000)
q = rand(1, 1000)
def generate_keypair(p, q, keysize):
    nMin = 1 << (keysize - 1)
    nMax = (1 << keysize) - 1
    primes = [2]
# we choose two prime numbers in range(start, stop) so that the difference of b it lengths is at most 2.
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
def encrypt(msg_plaintext, package):
    e, n = package
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    return msg_ciphertext

if __name__ == "__main__":
    bit_length = int(input("Enter bit_length: "))
    print("Running RSA...")
    print("Generating public/private keypair...")
    public, private ,p,q = generate_keypair(p, q, 2**bit_length)
    print("Public Key: ", public)
    print("Private Key: ", private)
    msg = input("Write msg: ")
    print([ord(c) for c in msg])
    encrypted_msg = encrypt(msg, public)
    print("Encrypted msg: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    num = int(input("Enter method to be used for decryption : 1 long integer factorization. 2 chinese remainder algorithm . 3 fault key generation "))
    if(num==1):
        print("The method you chose is long integer factorization by using primes")
        print("Decrypted msg: ")
        print(decrypt(encrypted_msg, private))
    elif(num==2):
        print("The method you chose is chinese remainder algorithm")
        decrypted_cipher = decrypt_rsa(p,q,private[0],encrypted_msg)
        print("Decrypted msg: ")
        print(str(decrypted_cipher))
    elif(num==3):
        print("The method you chose is fault key generation")
        decrypt_cipher = decrypt_fault(encrypted_msg,private)
        print(decrypt_cipher)