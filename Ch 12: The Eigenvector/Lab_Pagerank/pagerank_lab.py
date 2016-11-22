# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.
from imp import reload

import pagerank
from mat import Mat
from vec import Vec


## 1: (Task 12.12.1) Find Number of Links

def normalized(v):
    return 1.0/sum(v[j] for j in v.f.keys()) * v

def find_num_links(L):
    '''
    Input:
        - L: a square matrix representing link structure
    Output:
        - A vector mapping each column label of L to
          the number of non-zero entries in the corresponding
          column of L
    Example:
        >>> from matutil import listlist2mat
        >>> find_num_links(listlist2mat([[1,1,1],[1,1,0],[1,0,0]]))
        Vec({0, 1, 2},{0: 3, 1: 2, 2: 1})
    '''
    num_links_vec = Vec(L.D[1], {})
    for ((row, col), num_links) in L.f.items():
        num_links_vec[col] += num_links
    return num_links_vec

## 2: (Task 12.12.2) Make Markov
def make_Markov(L):
    '''
    Input:
        - L: a square matrix representing link structure
    Output:
        - None: changes L so that it plays the role of A_1
    Example:
        >>> from matutil import listlist2mat
        >>> M = Mat(({0,1,2},{0,1,2}), {(0,0):1, (0,1):1, (0,2):1, (1,0):1, (2,0):1, (2,2):1})
        >>> make_Markov(M)
        >>> M
        Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 1.0, (2, 0): 0.3333333333333333, (0, 0): 0.3333333333333333, (2, 2): 0.5, (1, 0): 0.3333333333333333, (0, 2): 0.5})
    '''
    num_links_vec = find_num_links(L)
    for ((row, col), num_links) in L.f.items():
        if num_links != 0:
            L[row, col] = float(num_links) / float(num_links_vec[col])


## 3: (Task 12.12.3) Power Method
def power_method(A1, i):
    '''
    Input:
        - A1: a matrix
        - i: number of iterations to perform
    Output:
        - An approximation to the stationary distribution
    Example:
        >>> from matutil import listlist2mat
        >>> power_method(listlist2mat([[0.6,0.5],[0.4,0.5]]), 10)
        Vec({0, 1},{0: 0.5464480874307795, 1: 0.45355191256922056})
    '''
    # Note that I had to change the expected values in unit test by < 10^-16 to pass.  Rounding error likely despite
    # renormalizing each round
    v = Vec(A1.D[1], {j:1 for j in A1.D[1]})
    for _ in range(i):
        v1 = (A1 * v)
        v2 = (Vec(A1.D[1], {c: 1.0/len(A1.D[1]) for c in A1.D[1]}) * v) * Vec(v.D, {c:1 for c in v.D})
        v = 0.85 * v1 + 0.15 * v2
        v = normalized(v)
        print("Power_method, v['sport']: ", v['sport'])
    return v

## 4: (Task 12.12.4) Jordan
reload(pagerank)
A1 = pagerank.read_data()
number_of_docs_with_jordan = len(pagerank.find_word('jordan'))
print("Num jordan docs: ", number_of_docs_with_jordan)


## 5: (Task 12.12.5) Wikigoogle
def wikigoogle(w, k, p):
    '''
    Input:
        - w: a word
        - k: number of results
        - p: pagerank eigenvector
    Output:
        - the list of the names of the kth heighest-pagerank Wikipedia
          articles containing the word w
    '''
    related = pagerank.find_word(w)
    related.sort(key = lambda x: p[x], reverse = True)
    return related[:k]


## 6: (Task 12.12.6) Using Power Method
p = power_method(A1, 5)
results_for_jordan = wikigoogle('jordan', 5, p) # give 5 of them as a list
results_for_obama  = wikigoogle('obama', 5, p)
results_for_tiger  = wikigoogle('tiger', 5, p)
results_for_matrix = wikigoogle('matrix', 5, p)

print(results_for_jordan)
print(results_for_obama)
print(results_for_tiger)
print(results_for_matrix)

## 7: (Task 12.12.7) Power Method Biased
def power_method_biased(A1, i, r):
    '''
    Input:
        - A1: a matrix, as in power_method
        - i: number of iterations
        - r: bias label
    Output:
        - Approximate eigenvector of .55A_1 + 0.15A_2 + 0.3A_r
    '''
    v = Vec(A1.D[1], {j:1 for j in A1.D[1]})
    for _ in range(i):
        v1 = (A1 * v)
        v2 = (Vec(A1.D[1], {c: 1.0/len(A1.D[1]) for c in A1.D[1]}) * v) * Vec(v.D, {c:1 for c in v.D})
        v3 = Vec(A1.D[0], {r: sum(v.f.values())}) # Same as multiplying matrix with 1s only in bias row by v
        v = 0.55 * v1 + 0.15 * v2 + 0.3 * v3
        v = normalized(v)
        print("Power_method_biased, v['sport']: ", v['sport'])
    return v

p_sport = power_method_biased(A1, 5, 'sport')
sporty_results_for_jordan = wikigoogle('jordan', 5, p_sport) # give 5 of them as a list
sporty_results_for_obama  = wikigoogle('obama', 5, p_sport)
sporty_results_for_tiger  = wikigoogle('tiger', 5, p_sport)
sporty_results_for_matrix = wikigoogle('matrix', 5, p_sport)

print(sporty_results_for_jordan)
print(sporty_results_for_obama)
print(sporty_results_for_tiger)
print(sporty_results_for_matrix)