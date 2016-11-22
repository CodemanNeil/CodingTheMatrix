# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from vecutil import list2vec


## 1: (Problem 8.6.1) Norm

norm1 = 3
norm2 = 4
norm3 = 3

def sigma(a, b):
    return (a*b)/(a*a)

## 2: (Problem 8.6.2) Closest Vector
# Write each vector as a list
# a = list2vec([1,2])
# b = list2vec([2,3])
# closest_vector_1 = sigma(a,b) * a
closest_vector_1 = [1.6, 3.2]

# a = list2vec([0,1,0])
# b = list2vec([1.414,1,1.732])
# closest_vector_2 = sigma(a,b) * a
closest_vector_2 = [0, 1 ,0]

# a = list2vec([-3,-2,-1,4])
# b = list2vec([7,2,5,0])
# closest_vector_3 = sigma(a,b) * a
closest_vector_3 = [3, 2, 1, -4]


## 3: (Problem 8.6.3) Projection Orthogonal to and onto Vectors
# Write each vector as a list
# round up to 6 decimal points if necessary
# a = list2vec([3,0])
# b = list2vec([2,1])
# project_onto_1 = sigma(a,b) * a
project_onto_1 = [2, 0]
# projection_orthogonal_1 = b - project_onto_1
projection_orthogonal_1 = [0, 1]

# a = list2vec([1.0,2.0,-1.0])
# b = list2vec([1,1,4])
# project_onto_2 = sigma(a,b) * a
project_onto_2 = [-1.0/6.0, -1.0/3.0, 1.0/6.0]
# projection_orthogonal_2 = b - project_onto_2
projection_orthogonal_2 = [7.0/6.0, 4.0/3.0, 23.0/6.0]

# a = list2vec([3,3,12])
# b = list2vec([1,1,4])
# project_onto_3 = sigma(a,b) * a
project_onto_3 = [1, 1, 4]
# projection_orthogonal_3 = b - project_onto_3
projection_orthogonal_3 = [0, 0, 0]
