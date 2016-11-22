# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.
import time

from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

import echelon

## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    return one if i%2 == 1 else 0

## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return Vec(primeset, {factor[0]:int2GF2(factor[1]) for factor in factors})

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a tuple (roots, rowlist)
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    Example:
        >>> from factoring_support import primes
        >>> N = 2419
        >>> primeset = primes(32)
        >>> roots, rowlist = find_candidates(N, primeset)
        >>> set(roots) == set([51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79])
        True
        >>> D = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        >>> set(rowlist) == set([Vec(D,{2: one, 13: one, 7: one}),\
                Vec(D,{3: one, 19: one, 5: one}),\
                Vec(D,{2: one, 3: one, 5: one, 13: one}),\
                Vec(D,{3: one, 5: one, 7: one}),\
                Vec(D,{7: one, 2: one, 3: one, 31: one}),\
                Vec(D,{3: one, 19: one}),\
                Vec(D,{2: one, 31: one}),\
                Vec(D,{2: one, 5: one, 23: one}),\
                Vec(D,{5: one}),\
                Vec(D,{3: one, 2: one, 19: one, 23: one}),\
                Vec(D,{2: one, 3: one, 5: one, 13: one}),\
                Vec(D,{2: one, 3: one, 13: one})])
        True
    '''
    roots = []
    rowlist = []
    x = intsqrt(N) + 2
    while len(roots) <= len(primeset):
        list_factors = dumb_factor(x**2 - N, primeset)
        if list_factors:
            roots.append(x)
            rowlist.append(make_Vec(primeset, list_factors))
        x += 1
    return roots, rowlist



## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    Example:
        >>> roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]
        >>> N = 2419
        >>> v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{1: one, 2: one, 11: one, 5: one})  
        >>> find_a_and_b(v, roots, N)
        (13498888, 778050)
        >>> v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: 0, 10: one, 2: one})
        >>> find_a_and_b(v, roots, N)
        (4081, 1170)
    '''
    alist = [roots[key] for key,value in v.f.items() if value == one]
    a = prod(alist)
    c = prod([x**2 - N for x in alist])
    b = intsqrt(c)
    assert b**2 == c
    return (a,b)

## Task 5
nontrivial_divisor_of_2461799993978700679 = None
N = 2461799993978700679
primelist = primes(10000)

start_long_time = time.time()
roots, rowlist = find_candidates(N, primelist)
M = echelon.transformation_rows(rowlist)
for row in reversed(M):
    a,b = find_a_and_b(row, roots, N)
    divisor = gcd(a-b, N)
    if divisor != 1 and divisor != N:
        nontrivial_divisor_of_2461799993978700679 = divisor
        break
elapsed_long_time = time.time() - start_long_time

print("Found nontrivial divisor: ", nontrivial_divisor_of_2461799993978700679, " inefficiently in time: ", elapsed_long_time)

nontrivial_divisor_of_2461799993978700679 = None
start_short_time = time.time()
roots, rowlist = find_candidates(N, primelist)
M = echelon.transformation_rows(rowlist, sorted(primelist, reverse=True))
for row in reversed(M):
    a,b = find_a_and_b(row, roots, N)
    divisor = gcd(a-b, N)
    if divisor != 1 and divisor != N:
        nontrivial_divisor_of_2461799993978700679 = divisor
        break
elapsed_short_time = time.time() - start_short_time

print("Found nontrivial divisor: ", nontrivial_divisor_of_2461799993978700679, " efficiently in time: ", elapsed_short_time)