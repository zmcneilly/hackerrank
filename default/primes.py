from math import *
from bitarray import bitarray

class PrimeNumbers():
    """
    This class is a special object for interacting with prime numbers
    """

    def update_prime(self, new_max):
        """
        This updates the object which contains the list of prime numbers
        """
        self.primes = bitarray(new_max)
        self.primes.setall(True)
        self.primes[0] = False
        self.primes[1] = False

        for i in xrange(2,int(sqrt(new_max)),1):
            if self.primes[i]:
                for j in xrange(i*i,new_max,i):
                    self.primes[j] = False

        self.MAX = int(new_max)

    def is_prime(self,num):
        """
        This method simply returns whether a number is prime or not
        """
        if num < 0:
            num = num*-1
        if num <= 1:
            return False
        if num % 2 == 0:
            return False
        if num > self.MAX:
            self.update_prime(num)
        return self.primes[num]

    def get_prime_list(self):
        return list(self.plist)

    def generate_prime_file(self):
        self.update_prime(1000000000)
        __f = open('primes.txt', 'w')
        self.primes.tofile(__f)
        __f.close()

    def load_prime_file(self):
        __f = open('primes.txt', 'r')
        self.primes = bitarray()
        self.primes.fromfile(__f)
        __f.close
        self.MAX = len(self.primes)


    def __init__(self, max_prime=10000):
        """
        This method is a constructor. If max_prime is passed it will set the
        list of primes up to 10,000.
        """
        self.MAX = 2
        self.primes = bitarray(max_prime+1)
        self.update_prime(max_prime)

