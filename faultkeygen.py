from random import randrange,randint
def miller_rabin(n, k):
    if n == 2:
        return True
    if not n & 1:
        return False
    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1
    s = 0
    d = n - 1
    for i in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True
# Multiplicative Inverse Calculation
def mod_inverse(a,m):
    a = a % m
    for i in range(1,m):
        if (a*i) % m == 1:
            return i
    return 1
# RSA Public Private Key Pair Generation
while True:
    p = randint(1,500)
    q = randint(1,500)
    if miller_rabin(p,64) and miller_rabin(q,64):
        tot = (p-1)*(q-1) # Euler's Totient function
        n = p*q # modulus
        break
while True:
    tot=15
    e = randint(10,tot-1) # public key
    if miller_rabin(e,64):
        break
priv_key = mod_inverse(e,tot) # private key
def encrypt_fault(n,e,data):
    return (data ** e) % n
def decrypt_fault(msg,a):
    d,n = a
    msg_p = [chr(pow(c, d, n)) for c in msg]
    return (''.join(msg_p))