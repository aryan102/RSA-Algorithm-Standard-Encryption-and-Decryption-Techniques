import argparse
#Variables
c,p,q,dp,dq = 0,0,0,0,0
#below function if used for argument parsing
def initiate_argparse():
    parser = argparse.ArgumentParser(description='Decryption tool for RSA Primes using the Chinese Remainder Theorem')
    parser.add_argument('--p', type=int, help='Input prime p used for RSA decryption')
    parser.add_argument('--q', type=int, help='Input prime q used for RSA Decryption')
    parser.add_argument('--dp', type=int, help='Input Chinese Remainder dp used for RSA decryption')
    parser.add_argument('--dq', type=int, help='Input Chinese Remainder dq used for RSA Decryption')
    parser.add_argument('--c', type=int, help='Input Cipher text to decrypt')
    return parser.parse_args()

def lcm(p, q):
    return p * q / gcd(p, q)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modular_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def decrypt_rsa(p,q,d,msg):
    dp = d%(p-1)
    dq = d%(q-1)
    qinv = modular_inverse(q, p)
    msg_plaintext = [chr(pow(c,dq,q)+(qinv*(pow(c,dp,p)-pow(c,dq,q)))%p) for c in msg]
    return(''.join(msg_plaintext))