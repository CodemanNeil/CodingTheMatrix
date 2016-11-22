# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.
from math import sqrt

from dictutil import dict2list, list2dict
from mat import Mat
from orthogonal_util import find_orthogonal_complement, orthogonalize, aug_orthogonalize
from read_data import read_vectors
from triangular import triangular_solve
from vec import Vec
from vecutil import list2vec
from matutil import listlist2mat, coldict2rowdict, rowdict2coldict, coldict2mat, mat2coldict, mat2rowdict, rowdict2mat

## 1: (Problem 9.11.1) Generators for orthogonal complement
U_vecs_1 = [list2vec([0,0,3,2])]
W_vecs_1 = [list2vec(v) for v in [[1,2,-3,-1],[1,2,0,1],[3,1,0,-1],[-1,-2,3,1]]]

# Give a list of Vecs
ortho_compl_generators_1 = find_orthogonal_complement(U_vecs_1, W_vecs_1)

U_vecs_2 = [list2vec([3,0,1])]
W_vecs_2 = [list2vec(v) for v in [[1,0,0],[1,0,1]]]

# Give a list of Vecs
ortho_compl_generators_2 = find_orthogonal_complement(U_vecs_2, W_vecs_2)

U_vecs_3 = [list2vec(v) for v in [[-4,3,1,-2],[-2,2,3,-1]]]
W_vecs_3 = [list2vec(v) for v in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]]

# Give a list of Vecs
ortho_compl_generators_3 = find_orthogonal_complement(U_vecs_3, W_vecs_3)



## 2: (Problem 9.11.3) Basis for null space
# Your solution should be a list of Vecs
A_vecs = [list2vec(v) for v in [[-4, -1, -3, -2], [0, 4, 0, -1]]]
R_vecs = [list2vec(v) for v in [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]]
null_space_basis = find_orthogonal_complement(A_vecs, R_vecs)



## 3: (Problem 9.11.9) Orthonormalize(L)
def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list Lstar of len(L) orthonormal Vecs such that, for all i in range(len(L)),
            Span L[:i+1] == Span Lstar[:i+1]

    >>> from vec import Vec
    >>> D = {'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> for v in orthonormalize(L): print(v)
    ...
    <BLANKLINE>
        a     b     c     d
    -----------------------
     0.73 0.548 0.183 0.365
    <BLANKLINE>
         a     b      c      d
    --------------------------
     0.187 0.403 -0.566 -0.695
    <BLANKLINE>
         a      b      c     d
    --------------------------
     0.528 -0.653 -0.512 0.181
    '''
    orthonormal_cols = []
    orthogonal_cols = orthogonalize(L)
    for col in orthogonal_cols:
        orthonormal_cols.append(col / (sqrt(col*col)))
    return orthonormal_cols



## 4: (Problem 9.11.10) aug_orthonormalize(L)
def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist of lists such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)

    >>> from vec import Vec
    >>> D={'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> Qlist, Rlist = aug_orthonormalize(L)
    >>> from matutil import coldict2mat
    >>> print(coldict2mat(Qlist))
    <BLANKLINE>
               0      1      2
         ---------------------
     a  |   0.73  0.187  0.528
     b  |  0.548  0.403 -0.653
     c  |  0.183 -0.566 -0.512
     d  |  0.365 -0.695  0.181
    <BLANKLINE>
    >>> print(coldict2mat(Rlist))
    <BLANKLINE>
              0    1      2
         ------------------
     0  |  5.48 8.03   9.49
     1  |     0 11.4 -0.636
     2  |     0    0   6.04
    <BLANKLINE>
    >>> print(coldict2mat(Qlist)*coldict2mat(Rlist))
    <BLANKLINE>
           0  1  2
         ---------
     a  |  4  8 10
     b  |  3  9  1
     c  |  1 -5 -1
     d  |  2 -5  5
    <BLANKLINE>
    '''
    Q_cols = []
    V_cols, R_cols = aug_orthogonalize(L)
    R_rows = coldict2rowdict(R_cols)
    for i, v_col in enumerate(V_cols):
        normalizer = sqrt(v_col * v_col)
        Q_cols.append(v_col / normalizer)
        R_rows[i] = normalizer * R_rows[i]
    return Q_cols, rowdict2coldict(R_rows)



## 5: (Problem 9.11.11) QR factorization of small matrices
#Compute the QR factorization

#Please represent your solution as a list of rows, such as [[1,0,0],[0,1,0],[0,0,1]]

#A = [list2vec(v) for v in [[6,2,3],[6,0,3]]]
#print("Part 1 Q")
#print(coldict2mat(aug_orthonormalize(A)[0]))
#print("\n Part 1 R")
#print(coldict2mat(aug_orthonormalize(A)[1]))

part_1_Q = [[0.857, 0.256], [0.286, -0.958], [0.429, 0.128]]
part_1_R = [[7, 6.43], [0, 1.92]]

#A2 = [list2vec(v) for v in [[2,2,1],[3,1,1]]]
#print("\n")
#print("Part 2 Q")
#print(coldict2mat(aug_orthonormalize(A2)[0]))
#print("\n Part 2 R")
#print(coldict2mat(aug_orthonormalize(A2)[1]))

part_2_Q = [[0.667, 0.707], [0.667, -0.707], [0.333, 0]]
part_2_R = [[3, 3], [0, 1.41]]

## 6: (Problem 9.11.12) QR Solve
def QR_factor(A):
    col_labels = sorted(A.D[1], key=repr)
    Acols = dict2list(mat2coldict(A),col_labels)
    Qlist, Rlist = aug_orthonormalize(Acols)
    #Now make Mats
    Q = coldict2mat(Qlist)
    R = coldict2mat(list2dict(Rlist, col_labels))
    return Q,R


def QR_solve(A, b):
    '''
    Input:
        - A: a Mat with linearly independent columns
        - b: a Vec whose domain equals the set of row-labels of A
    Output:
        - vector x that minimizes norm(b - A*x)
    Note: This procedure uses the procedure QR_factor, which in turn uses dict2list and list2dict.
           You wrote these procedures long back in python_lab.  Make sure the completed python_lab.py
           is in your matrix directory.
    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR_factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = QR_solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result.is_almost_zero()
        True
    '''
    Q, R = QR_factor(A)
    return triangular_solve(mat2rowdict(R), sorted(A.D[1],key=repr), Q.transpose() * b)


## 7: (Problem 9.11.13) Least Squares Problem
# Please give each solution as a Vec

least_squares_A1 = listlist2mat([[8, 1], [6, 2], [0, 6]])
least_squares_Q1 = listlist2mat([[.8,-0.099],[.6, 0.132],[0,0.986]])
least_squares_R1 = listlist2mat([[10,2],[0,6.08]])
least_squares_b1 = list2vec([10, 8, 6])

#print(QR_solve(least_squares_A1, least_squares_b1))

x_hat_1 = Vec({0,1}, {0:1.08, 1:0.984})


least_squares_A2 = listlist2mat([[3, 1], [4, 1], [5, 1]])
least_squares_Q2 = listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
least_squares_R2 = listlist2mat([[7.07, 1.7],[0,.346]])
least_squares_b2 = list2vec([10,13,15])

#print(QR_solve(least_squares_A2, least_squares_b2))

x_hat_2 = Vec({0,1}, {0:2.5, 1:2.67})



## 8: (Problem 9.11.14) Small examples of least squares
#Find the vector minimizing (Ax-b)^2

#Please represent your solution as a list

least_squares_A3 = listlist2mat([[3, 1], [4, 1]])
least_squares_b3 = list2vec([10,13])

your_answer_1 = [1.08, 0.984]
your_answer_2 = [3,1]

#your_answer_1 = QR_solve(least_squares_A1, least_squares_b1)
#your_answer_2 = QR_solve(least_squares_A3, least_squares_b3)

## 9: (Problem 9.11.15) Linear regression example
#Find a and b for the y=ax+b line of best fit

data_vecs = read_vectors("age-height.txt")
age_vecs_row_dict = {}
height_vec = Vec(set(range(len(data_vecs))), {})
for i, data_vec in enumerate(data_vecs):
    age_vecs_row_dict[i] = list2vec([data_vec['age'], 1])
    height_vec[i] = data_vec['height']
A = rowdict2mat(age_vecs_row_dict)
x_hat = QR_solve(A, height_vec)
a = 0.6349650349650302
b = 64.9283216783218
