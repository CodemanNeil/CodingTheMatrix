# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.
import time

from cancer_data import read_training_data
from mat import *
from vec import *

## Task 1 ##
from vecutil import list2vec


def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    return Vec(u.D, {key : 1 if u[key] >= 0 else -1 for key in u.D})

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> fraction_wrong(A, b, w)
        0.3333333333333333
    '''
    (signum(A*w) - b)
    return sum(0 if (signum(A*w) - b)[key] == 0 else 1 for key in (b.D))/len(b.D)

## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> loss(A, b, w)
        317
    '''
    return sum((A*w - b)[key]**2 for key in b.D)

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> find_grad(A, b, w) == Vec({'B', 'A'},{'B': -290, 'A': 60})
        True
    '''
    return 2 * (A*w - b) * A

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> sigma = .1
        >>> gradient_descent_step(A, b, w, sigma) == Vec({'B', 'A'},{'B': 27.0, 'A': -5.0})
        True
    '''
    return w - sigma * find_grad(A, b, w)

## Ungraded task ##
def gradient_descent(A, b, w, sigma, T):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
        - T: number of iterations to run
    Output: hypothesis vector obtained after T iterations of gradient descent.
    '''
    # start_time = time.time()
    for i in range(T):
        w = gradient_descent_step(A, b, w, sigma)
        # if i % 30 == 0:
            # print_statistics(A, b, w)
    # elapsed_time = time.time() - start_time
    #print("Elapsed time running ", T, " iterations: ", elapsed_time)
    return w

def print_statistics(A, b, w):
    print("Loss function: ", loss(A, b, w))
    print("Percent wrong: ", fraction_wrong(A, b, w))

if __name__ == '__main__':
    A_train, b_train = read_training_data('train.data')
    w_0 = Vec(A_train.D[1], {col : 0 for col in A_train.D[1]})
    w_1 = Vec(A_train.D[1], {col : 1 for col in A_train.D[1]})
    step_a = 10**(-9)
    step_b = 2*10**(-9)

    hyp_0a = gradient_descent(A_train, b_train, w_0, step_a, 1000)
    print("Statistics for initial weights 0, step size 10^-9:")
    print_statistics(A_train, b_train, hyp_0a)

    hyp_1a = gradient_descent(A_train, b_train, w_1, step_a, 1000)
    print("Statistics for initial weights 1, step size 10^-9:")
    print_statistics(A_train, b_train, hyp_0a)

    hyp_0b = gradient_descent(A_train, b_train, w_0, step_b, 1000)
    print("Statistics for initial weights 0, step size 2*10^-9:")
    print_statistics(A_train, b_train, hyp_0a)

    hyp_1b = gradient_descent(A_train, b_train, w_1, step_b, 1000)
    print("Statistics for initial weights 1, step size 2*10^-9:")
    print_statistics(A_train, b_train, hyp_0a)