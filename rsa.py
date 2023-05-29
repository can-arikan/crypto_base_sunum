
from prime import chosePub, primeGenerator

p = primeGenerator(1024)
q = primeGenerator(1024)

while q == p:
    q = primeGenerator(1024)

n = p * q

phiN = (p-1) * (q-1)

# Choose an encryption exponent, e:
# publickey must be a positive integer less than φ(n) and relatively prime to φ(n).

public_key = chosePub(p, q)
private_key = pow(public_key, -1, phiN)

# Moray bana bir mesaj atmak istiyorsa :D

message = b"merhaba can nasilsin" # messaj n den küçük olmalı

int_message = int.from_bytes(message, byteorder='big')

encrypted_message = pow(int_message, public_key, n)

print("\n\nEncrpted Message: ", encrypted_message.to_bytes(length=(encrypted_message.bit_length() + 7) // 8, byteorder='big'), end='\n\n\n')

# Bana bu mesaji yolladı

decrypted_message = pow(encrypted_message, private_key, n)

byte_message = decrypted_message.to_bytes(length=(decrypted_message.bit_length() + 7) // 8, byteorder='big')

string_message = byte_message.decode('UTF-8')

print(string_message, end='\n\n')