from hashlib import sha256
import random

from prime import gen_primes_bit, mod_inverse

p, q, g = gen_primes_bit(1024)

privkey = random.randint(0, p - 1)
pubkey = pow(g, privkey, p)

message = b"Merhabalar :D"
hash = sha256(message).digest()
hash = int.from_bytes(hash, byteorder='big')

print(hash)

while True:
    k = random.randint(2, q - 1)
    r = pow(pow(g, k, p), 1, q)
    if r != 0:
        break

inv_k = mod_inverse(k, q)
s = (inv_k * (hash + privkey * r)) % q
print(s, r)

if r < 1 or r > q - 1 or s < 1 or s > q - 1:
    raise Exception("False Values")

w = mod_inverse(s, q)
u1 = (hash * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(pubkey, u2, p)) % p) % q

print(int.from_bytes(sha256(message).digest()) == hash)
print(v == r, r, v)