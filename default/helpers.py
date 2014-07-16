#!env/bin/python
from math import sqrt,floor,log10,factorial
import decimal,random
from itertools import combinations
from bitarry import bitarray
collatz_cache = {}

def triangle_num(n):
  i = 0;
  result = 0;
  while i <= n:
    result += i
    i += 1
  return result

def find_factors(n):
  if n < 0:
      n = n * -1
  factors=[]
  MAX = int(sqrt(n))+1
  for i in range(2,MAX,1):
    if n % i == 0:
      factors.append(i)
      factors.append(n/i)
  return factors

def is_prime(n):
    if n < 0:
        n = n*-1
    if n <= 1:
        return False
    elif n == 2:
        return True
    if n % 2 == 0:
        return False
    MAX = int(sqrt(n))+1
    for i in range(3,MAX,2):
        if n % i == 0:
            return False
    return True

def find_primes(MAX):
    primes = bitarray(MAX+1)
    primes.setall(True)

    for i in range(2,int(sqrt(MAX))+1,1):
      if primes[i]:
        for j in xrange(i*i,MAX+1,i):
          primes[j] = False

    return primes

def collatz_seq(n):
    result = []
    if n == 1:
        result.append(1)
    elif n % 2 == 0:
        result.append(n)
        result.extend(collatz_seq(n/2))
    else:
        result.append(n)
        n1 = (3*n)+1
        result.append(n1)
        result.extend(collatz_seq((n1)/2))
    return result

def collatz_cnt(n):
    if n in collatz_cache:
        return collatz_cache[n]
    if n == 1:
        collatz_cache[n] = 1
    elif n % 2 == 0:
        collatz_cache[n] = 1+collatz_cnt(n/2)
    else:
        collatz_cache[n] = 1+collatz_cnt(3*n+1)
    return collatz_cache[n]

def n_choose_r(n,r):
    """How many combinations with r items can be made from the n given items"""
    return factorial(n)/(factorial(r)*factorial(n-r))

def sum_of_digits(n):
    """Return the sum of the digits of the number"""
    o = str(n)
    result = 0
    for x in o:
        result += int(x)
    return result

def sum_of_divisors(n):
    result = 0
    for x in find_factors(n):
        if x < n:
            result += x
    return result

def is_amicable(n):
    result = -1
    dn = sum_of_divisors(n)
    dn1 = sum_of_divisors(dn)
    if n == dn1 and dn != dn1:
        result = dn
    return result

def alphabetic_value(name):
    lname = name.lower()
    result = 0
    for char in lname:
        result += ord(char) - 96
    return result

def is_abundant(n):
    result = 1
    MAX = int(sqrt(n))
    for i in range(2,MAX+1,1):
      if n % i == 0:
        result+=i
        if i != (n/i):
            result+=(n/i)
        if result > n:
            return True
    return False

def o_is_abundant(n):
    result = 0
    for x in set(find_factors(n)):
        if x < n:
            result += x
    if result > n:
        return True
    else:
        return False 

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs,low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]
        
def zmute(s, goal):
    if len(s) == 1:
        return s[0]
    elif goal == 1:
        result = ''
        for x in s:
            result = result+str(x)
        return result
    else:
        steps = factorial(len(s)-1)
        if goal >= steps:
            pos = ((goal-1) / steps)
            goal = goal - (steps*pos)
        else:
            pos = 0
        s0 = s[pos]
        s1 = []
        for x in s:
            if x != s0:
                s1.append(x)
        return str(s0)+str(zmute(s1,goal))


def fibonacci_r(n):
    """This is an implementation of Wikipedia's formula for estimating a
    Fibonacci number at index 'n' through use of rounding"""
    phi = (1 + sqrt(5))/2
    if n >= 0:
        return \
        ((pow(decimal.Decimal(phi),decimal.Decimal(n))/decimal.Decimal(sqrt(5)))+\
        decimal.Decimal(.5)).to_integral_exact(rounding=decimal.ROUND_FLOOR)
    else:
        return 0

def num_digits(n):
    """This function is intended to return the number of digits of n"""
    d = decimal.Decimal(n)
    l = d.log10().to_integral_exact(rounding=decimal.ROUND_FLOOR)
    return l + 1

def is_circular_prime(n):
    if not is_prime(n):
        return False
    o = n
    n = ((n % 10)*(10**int(log10(n))))+(n/10)
    while o != n:
        if not is_prime(n):
            return False
        else:
            n = ((n % 10)*(10**int(log10(n))))+(n/10)
    return True

def digit_to_char(digit):
    if digit < 10:
      return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
      return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)

def is_palindrome(n):
    rn = str(n)[::-1]
    return rn == str(n)

def is_pandigital(n):
    for i in range(1,10):
        if i not in str(n):
            return False
    return True

def common_factors(n,m):
    """Returns the first factors between n and m"""
    result = []
    if n < m:
        MAX = int(sqrt(n))
        if m % n == 0:
            result.append(n)
    else:
        MAX = int(sqrt(m))
        if n % m == 0:
            result.append(m)
    for x in range(2,MAX+1):
        if n % x == 0 and m % x == 0:
            result.append(x)
            if n % (n/x) == 0 and m % (n/x) == 0:
                result.append(n/x)
            if n % (m/x) == 0 and m % (m/x) == 0:
                result.append(m/x)
    return result

def triangle_num(n):
    return (n*(n+1))/2

def test_triable_num(x):
    n = (sqrt(8*x+1)-1)/2
    return n >= 1 and n % 1 == 0

def pentagonal_num(n):
    return n*(3*n-1)/2

def test_pentagonal_num(x):
    n = (sqrt(24*x+1)+1)/6
    return n >= 1 and n % 1 == 0

def hexagonal_num(n):
    return n*(2*n-1)

def test_hexagonal_num(x):
    n = (sqrt(8*x+1)+1)/4
    return n >= 1 and n % 1 == 0

def distinct_prime_factors(n,pset):
    """n is a positive intger
    pset is a set of prime numbers
    this returns a list of distinct, prime, factors of n"""
    #factors = find_factors(n)
    if n in pset or n < 2:
        return []
    x = 2
    factors = []
    while n % x != 0:
        x += 1
    factors.append(x)
    factors.append(n/x)
    result = []
    for f in factors:
        if f in pset:
            result.append(f)
        else:
            result.extend(distinct_prime_factors(f,pset))
    return list(set(result))

def num_dpf(n,pset):
    result = 0
    plist = list(pset)
    plist.sort()
    if n in pset:
        return result
    else:
        for x in plist:
            if x > sqrt(n):
                break
            if n % x == 0:
                result += 2
    return result

def trim_left_int(n):
    return n % (10**int(log10(n)))

def trim_right_int(n):
    return int(n/10)

def nCr(l,n):
    s = ''
    for e in l:
        s = s + str(e)
    return combinations(s,n)

def change_base(n,bi,bf):
    """This function converts the string n from the base bi to the base bf"""
    l = list(n)
    t = 0
    for x in xrange(0,len(l)):
        t += bi**x * int(l[len(l)-1-x])
    return str_base(t,bf)
