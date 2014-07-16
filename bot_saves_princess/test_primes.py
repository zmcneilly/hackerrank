from primes import *

pn = PrimeNumbers(100)

if pn.is_prime(1):
    print "is_prime does not work with n = 1"

if pn.is_prime(-1):
    print "is_prime does not work with n = -1"

if not pn.is_prime(-2):
    print "is_prime does not work with n = -2"

if not pn.is_prime(2):
    print "is_prime does not work with n = 2"

pn.update_prime(1000)

pn.get_prime_list()

pn.is_prime(10000)
