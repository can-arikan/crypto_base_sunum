from hashlib import sha256

p = 800964073725231779968797423322791145896394398183
q = 121792652374353214004351839200620599317827646201001564618119236063683944373717615394358963785027440359017583791876181112466202879854799107758650991466003442179816830180146354095081429140037614275881107644595410455024024813165614248571188347470498409000402825184845181161515900720280201678227760417106064219
h = 5
g = pow(h, int((p - 1) / q), p)

privkey = 42
pubkey = pow(g, privkey, p)

print(g, privkey, pubkey)

message = b"Merhabalar sevgili arkadaslar"
h = sha256(message)

print(h)

k = 40 # Must be lower than q - 1

r = pow(pow(g, k, p), 1, q)
inv_k = pow(k, -1, q)
tmp = (h + (privkey * r))
s = pow(inv_k*tmp, 1, q)
print(s, r)

# At this point lets assume i want to verify and i know message it self, p, q, g, pubkey, r and s

w = pow(int(s), -1, int(q))
u1 = pow((h*w), 1, q)
u2 = pow((r*w), 1, q)
v = pow(pow(pow(g, u1) * pow(pubkey, u2), 1, p), 1, q)

print(sha256(message) == h)
print(v == r, r, v)