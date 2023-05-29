from poly import evaluate
from scipy.interpolate import lagrange

private = [106, 77, 108]

user1_secret = (1, evaluate(private, 1))
user2_secret = (2, evaluate(private, 2))
user3_secret = (3, evaluate(private, 3))
user4_secret = (4, evaluate(private, 4))
user5_secret = (5, evaluate(private, 5))
user6_secret = (6, evaluate(private, 6))

poly = lagrange(
    [
        user1_secret[0],
        user2_secret[0],
        user3_secret[0],
        user4_secret[0],
    ],
    [
        user1_secret[1],
        user2_secret[1],
        user3_secret[1],
        user4_secret[1],
    ],
)

coefs = list(poly.c)

secret = int(coefs[len(coefs) - 1])

print("\n\nsecret: {}\n\n".format(secret))

poly = lagrange(
    [
        user1_secret[0],
        user2_secret[0],
        user4_secret[0],
    ],
    [
        user1_secret[1],
        user2_secret[1],
        user4_secret[1],
    ], 
)

coefs = list(poly.c)

secret = int(coefs[len(coefs) - 1])

print("\n\nsecret: {}\n\n".format(secret))

poly = lagrange(
    [
        user6_secret[0],
        user5_secret[0],
        user4_secret[0],
    ],
    [
        user6_secret[1],
        user5_secret[1],
        user4_secret[1],
    ], 
)

coefs = list(poly.c)

secret = int(coefs[len(coefs) - 1])

print("\n\nsecret: {}\n\n".format(secret))