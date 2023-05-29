from phe import paillier

def send(x):
    ""

def ExampleMtA():
    public_key, private_key = paillier.generate_paillier_keypair()

    alice_pk_data = 15
    bob_pk_data = 25

    # Alice Sends to Bob
    c1 = public_key.encrypt(alice_pk_data)
    c1.obfuscate()
    send(c1)

    # Bob multiply it with his private and add random value;than sends to Alice
    random_m = 106

    c2 = c1 * bob_pk_data + random_m
    c2.obfuscate()
    send(c2)

    """
    At this point bob knows c1, m and alice knows c2
    alice decrpypt c2 and get (ab + m) lets say a_prime
    bob calculates -m lets say b_prime
    they share a_prime and b_prime with each other
    where a_prime + b_prime = a * b which is the secret that we are looking for
    """

    b_prime = -random_m

    a_prime = private_key.decrypt(c2)

    print(a_prime + b_prime)
    print(alice_pk_data * bob_pk_data)

ExampleMtA()