# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from independence import rank



## 1: (Task 7.7.1) Choosing a Secret Vector
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    is_u_valid = False
    u = list2vec([])
    while not is_u_valid:
        u = generate_secret_vector()
        if a0*u == s and b0*u == t:
            is_u_valid = True
    return u

def generate_secret_vector():
    return list2vec([randGF2() for _ in range(6)])

def generate_sharing_vectors():
    are_vectors_independent = False
    list_vectors = []
    while not are_vectors_independent:
        list_vectors = [generate_secret_vector() for _ in range(8)]
        are_vectors_independent = True

        first_group = list_vectors[0:6]                       # a1,b1,a2,b2,a3,b3
        second_group = list_vectors[0:4] + list_vectors[4:6]  # a1,b1,a2,b2,a4,b4
        third_group = list_vectors[0:2] + list_vectors[2:6]   # a2,b2,a3,b3,a4,b4
        if rank(first_group) != 6 or rank(second_group) != 6 or rank(third_group) != 6:
            are_vectors_independent = False
    return list_vectors

## 2: (Task 7.7.2) Finding Secret Sharing Vectors
# Give each vector as a Vec instance
secret_a0 = list2vec([one,one,0,one,0,one])
secret_b0 = list2vec([one,one,0,0,0,one])
secret_a1 = list2vec([0,0,one,0,0,0])
secret_b1 = list2vec([0,0,0,one,0,0])
secret_a2 = list2vec([0,one,0,one,0,0])
secret_b2 = list2vec([0,one,one,one,0,one])
secret_a3 = list2vec([one,one,0,one,0,one])
secret_b3 = list2vec([one,0,one,0,one,one])
secret_a4 = list2vec([one,0,one,one,0,one])
secret_b4 = list2vec([one,0,0,0,one,0])

