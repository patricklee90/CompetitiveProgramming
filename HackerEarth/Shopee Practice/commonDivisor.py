'''
Question Link: https://www.hackerrank.com/challenges/common-divisors/problem 

Solution Explanation: https://www.geeksforgeeks.org/common-divisors-of-two-numbers/ 

'''
import math
 
# Map to store the count of each
# prime factor of a
ma = {}
 
# Function that calculate the count of
# each prime factor of a number
def primeFactorize(a):
     
    sqt = int(math.sqrt(a))
    for i in range(2, sqt, 2):
        cnt = 0
         
        while (a % i == 0):
            cnt += 1
            a /= i
             
        ma[i] = cnt
         
    if (a > 1):
        ma[a] = 1
         
# Function to calculate all common
# divisors of two given numbers
# a, b --> input integer numbers
def commDi1(a, b):
     
    # Find count of each prime factor of a
    primeFactorize(a)
     
    # stores number of common divisors
    res = 1
     
    # Find the count of prime factors
    # of b using distinct prime factors of a
    for key, value in ma.items():
        cnt = 0
         
        while (b % key == 0):
            b /= key
            cnt += 1
             
        # Prime factor of common divisor
        # has minimum cnt of both a and b
        res *= (min(cnt, value) + 1)
         
    return res
     
# Function to calculate gcd of two numbers
def gcd(a, b):
     
    if a == 0:
        return b
    return gcd(b % a, a)
   
# Function to calculate all common divisors
# of two given numbers
# a, b --> input integer numbers
def commDiv(a, b):
     
    # find GCD of a, b
    n = gcd(a, b)
 
    # Count divisors of n
    result = 0
    for i in range(1,int(math.sqrt(n))+1):
 
        # if i is a factor of n
        if n % i == 0:
 
            # check if divisors are equal
            if n/i == i:
                result += 1
            else:
                result += 2
                 
    return result

a = 288
b = 240
print(commDiv(a, b))