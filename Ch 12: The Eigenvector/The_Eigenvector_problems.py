# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec



## 1: (Problem 12.14.1) Finding eigenvalues and -vectors
# Provide eigenvectors as lists.
# If there is only one eigenvalue for a part,
#   use None for one of them

# Part a
p1_part_a_eigenvalue1 = 2
p1_part_a_eigenvector1 = [1, 1/2]
p1_part_a_eigenvalue2 = -1
p1_part_a_eigenvector2 = [-1, 1]

# Part b
p1_part_b_eigenvalue1 = 4
p1_part_b_eigenvector1 = [1, 3]
p1_part_b_eigenvalue2 = 0
p1_part_b_eigenvector2 = [1, -1]

# Part c
p1_part_c_eigenvalue1 = 6
p1_part_c_eigenvector1 = [1, 0]
p1_part_c_eigenvalue2 = 6
p1_part_c_eigenvector2 = [0, 1]

# Part d
p1_part_d_eigenvalue1 = 4
p1_part_d_eigenvector1 = [1, 1]
p1_part_d_eigenvalue2 = 0
p1_part_d_eigenvector2 = [1, 0]




## 2: (Problem 12.14.2) Finding eigenvectors
# Provide eigenvectors as lists.


# Part a
p2_part_a_lambda1_eigenvector = [2, 1]
p2_part_a_lambda2_eigenvector = [1, 1]

# Part b
p2_part_b_lambda1_eigenvector = [0, 1, 1]
p2_part_b_lambda2_eigenvector = [0, 1, -1]



## 3: (Problem 12.14.3) Finding the eigenvalue associated with an eigenvector
# Part a
p3_part_a_eigenvalue1 = -1
p3_part_a_eigenvalue2 = 5

# Part b
p3_part_b_eigenvalue1 = 2
p3_part_b_eigenvalue2 = 5



## 4: (Problem 12.14.11) Markov chains and eigenvectors
D = {'S', 'R', 'F', 'W'}
transition_matrix = Mat((D, D),
                        {('S','S'): 0.5, ('S','R'): 0.2, ('S','F'): 0.0, ('S','W'): 0.1,
                         ('R','S'): 0.2, ('R','R'): 0.6, ('R','F'): 0.0, ('R','W'): 0.0,
                         ('F','S'): 0.0, ('F','R'): 0.2, ('F','F'): 0.4, ('F','W'): 0.8,
                         ('W','S'): 0.3, ('W','R'): 0.0, ('W','F'): 0.6, ('W','W'): 0.1})

definitely_windy_vector = Vec(D, {'W':1})

day_after_windy = Vec(D, {'S': 0.1, 'R': 0.0, 'F': 0.8, 'W': 0.1})

uniform = Vec(D, {'S': 0.25, 'R': 0.25, 'F': 0.25, 'W': 0.25})
day_after_uniform = transition_matrix * uniform
print(day_after_uniform)

#four_hundred_days_from_now = uniform
#for _ in range(40000):
#    four_hundred_days_from_now = transition_matrix * four_hundred_days_from_now

four_hundred_days_from_now = Vec(D, {'S': 0.0909, 'R': 0.0455, 'F': 0.5, 'W': 0.364})

# Be clever here; no computation is needed:
eigenvalue = 1
eigenvector = Vec(D, {'S': 0.0909, 'R': 0.0455, 'F': 0.5, 'W': 0.364}) # as an instance of Vec
# Stationary distribution has max eigenvalue of 1
