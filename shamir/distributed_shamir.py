import random
import numpy as np
from scipy.interpolate import lagrange

def generate_shares(n, k, prime):
    coefficients = [random.randint(1, prime - 1)] + [random.randint(1, prime - 1) for _ in range(k - 1)]
    shares = []

    for i in range(1, n + 1):
        share = 0
        for j in range(k):
            coefficient = coefficients[j]
            share += coefficient * (i ** j)

        shares.append((i, share % prime))

    shares.append((0, coefficients[0]))

    return shares

def reconstruct_secret(shares, k, prime):
    points = shares[:k]
    x_values = np.array([x for x, _ in points])
    y_values = np.array([y for _, y in points])

    poly = lagrange(x_values, y_values)
    coefficients = np.round(poly.coefficients) % prime
    secret = int(coefficients[len(coefficients) - 1]) % prime

    return secret

# Example usage
n = 5
k = 3
prime = 257

# Generate shares
shares = [generate_shares(n, k, prime) for _ in range(n)]
print("Shares:")
for i in range(n):
    print("--------------------")
    print(f"N: {i}, Secret: {shares[i][n]}")
    print("--------------------")
    for x, y in shares[i]:
        print(f"Participant {x}: {y}")

final_secret = 0

# Reconstruct secret
for i in range(n):
    reconstructed_secret = reconstruct_secret(shares[i], k, prime)
    final_secret = pow((final_secret + reconstructed_secret), 1, prime)
    print(f"\nReconstructed Secret: {reconstructed_secret}")

print(f"\nCommon Private: {final_secret}")