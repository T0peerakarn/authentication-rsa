import random

class Rsa:

  def __init__(self, n = 512):
    """
      a function to initialize the object
      by creating a n-bits public key
      and a n-bits private key
    """

    self.public_key, self.private_key = self.generate_key(n)

  def inverse_modular(self, a, b):
    """
      a function returns a tuple (x, y, gcd(a, b))
      such that ax + by = gcd(a, b)
    """

    if a % b == 0:
      return 0, 1, b
    
    x, y, gcd = self.inverse_modular(b, a % b)
    return y, x - (a // b) * y, gcd
  
  def modular_exponential(self, a, m, n):
    """
      a function to calculate (a ^ m) % n
      in O(log(m))
    """

    res = 1
    for b in bin(m)[2:]:

      res = (res * res) % n

      if b == "1":
        res = (res * a) % n

    return res

  def primality_test(self, n, k = 128):
    """
      a function to check whether the given number n
      is prime number or not
      
      using the Miller-Rabin for k iterations
    """

    # return False if n <= 1
    if n <= 1:
      return False
    
    # return True if n == 2
    if n == 2:
      return True

    # find s, q such that n-1 = q * (2 ^ s)
    s, q = 0, n - 1
    while (q & 1) == 0:

      s += 1
      q >>= 1

    # Miller-Rabin test for k iterations
    for _ in range(k):

      a = random.randint(1, n-1)
      x = self.modular_exponential(a, q, n)

      if x != 1:

        i = 1
        while i < s and x != n-1:
          x = (x * x) % n
          i += 1

        if x != n-1:
          return False
        
    return True

  def generate_prime(self, n):
    """
      a function to generate a n-bits prime number
    """

    while True:

      # get a random n-bits number
      p = random.getrandbits(n)

      # check whether p is prime or not
      # if so, return p
      # otherwise, random a new p
      if self.primality_test(p):
        return p

  def generate_key(self, n):
    """
      a function generate a public key and private key
      both keys have length of n-bits
    """

    p = self.generate_prime(n)
    q = self.generate_prime(n)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    while True:
      e = random.randint(1, phi_n - 1)
      d, _, gcd = self.inverse_modular(e, phi_n)

      if gcd == 1:
        return (e, n), (d % phi_n, n)
  
  def encrypt(self, m):
    """
      a function to encrypt the plain message m
      using the generated public key
    """
    
    return self.modular_exponential(m, self.public_key[0], self.public_key[1])

  def decrypt(self, c):
    """
      a function to decrypt the ciphered message c
      using the generated private key
    """

    return self.modular_exponential(c, self.private_key[0], self.private_key[1])
