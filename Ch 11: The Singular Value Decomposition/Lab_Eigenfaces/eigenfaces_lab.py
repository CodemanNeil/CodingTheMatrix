# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.
import eigenfaces
from image import image2display
from matutil import rowdict2mat, mat2coldict
from svd import factor
from vec import Vec


def find_centroid(veclist):
    '''
    Input:
        - veclist: a list of Vecs
    Output:
        - a Vec, the centroid of veclist
    Example:
        >>> from vecutil import list2vec
        >>> vs = [list2vec(l) for l in [[1,2,3],[2,3,4],[9,10,11]]]
        >>> find_centroid(vs)
        Vec({0, 1, 2},{0: 4.0, 1: 5.0, 2: 6.0})
    '''
    num_vecs = len(veclist)
    vec = {}
    for r in veclist[0].D:
        avg = 0
        for n in range(num_vecs):
            avg += veclist[n][r]
        avg = avg/num_vecs
        vec[r] = avg
    return Vec(veclist[0].D, vec)

def get_dict_of_image_vecs(path, n=20):
    images_dict = eigenfaces.load_images(path, n)
    D = {(x,y) for x in range(166) for y in range(189)}
    return {n : Vec(D, {(x,y) : images_dict[n][y][x] for x in range(166) for y in range(189)}) for n in images_dict}

def get_listlist_from_image_vec(image_vec):
    image = []
    for y in range(189):
        image_row = []
        for x in range(166):
            image_row.append(image_vec[x,y])
        image.append(image_row)
    return image

## Task 1

# see documentation of eigenfaces.load_images

face_images = get_dict_of_image_vecs('faces') # dict of Vecs

## Task 2

centroid = find_centroid(list(face_images.values()))
centered_face_images = {n : face_image - centroid for n,face_image in face_images.items()}


## Task 3

A = rowdict2mat(centered_face_images) # centered image vectors
U,S,V = factor(A)
V_cols = mat2coldict(V)
orthonormal_basis = rowdict2mat([V_cols[i] for i in range(10)]) # 10 rows

## Task 4

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def projected_representation(M, x):
    '''
    Input:
        - M: a matrix with orthonormal rows with M.D[1] == x.D
        - x: a vector
    Output:
        - the projection of x onto the row-space of M
    Examples:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0, 0], [0, 1, 0]])
        >>> projected_representation(M, x)
        Vec({0, 1},{0: 1, 1: 2})
        >>> M = listlist2mat([[3/5, 1/5, 1/5], [0, 2/3, 1/3]])
        >>> projected_representation(M, x)
        Vec({0, 1},{0: 1.6, 1: 2.333333333333333})
    '''
    return M*x

## Task 5

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def projection_length_squared(M, x):
    '''
    Input:
        - M: matrix with orthonormal rows with M.D[1] == x.D
        - x: vector
    Output:
        - the square of the norm of the projection of x into the
          row-space of M
    Example:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0, 0], [0, 1, 0]])
        >>> projection_length_squared(M, x)
        5
        >>> M = listlist2mat([[3/5, 1/5, 1/5], [0, 2/3, 1/3]])
        >>> projection_length_squared(M, x)
        5.644424691358024
    '''
    proj_x_coord = projected_representation(M, x)
    proj_x = proj_x_coord * M
    return proj_x * proj_x

## Task 6

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def distance_squared(M, x):
    '''
    Input:
        - M: matrix with orthonormal rows with M.D[1] == x.D
        - x: vector
    Output:
        - the square of the distance from x to the row-space of M
    Example:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0, 0], [0, 1, 0]])
        >>> distance_squared(M, x)
        9
        >>> M = listlist2mat([[3/5, 1/5, 1/5], [0, 2/3, 1/3]])
        >>> distance_squared(M, x)
        8.355575308641976
    '''
    return x*x - projection_length_squared(M, x)

## Task 7

distances_to_subspace = [distance_squared(orthonormal_basis, centered_face) for centered_face in centered_face_images.values()]

## Task 8

unclassified_images = get_dict_of_image_vecs('unclassified', 11)
centered_unclassified_images = {n : unclassified_image - centroid for n,unclassified_image in unclassified_images.items()}

unclassified_distances_to_subspace = [distance_squared(orthonormal_basis, centered_unclassified) for centered_unclassified in centered_unclassified_images.values()]

print("Face distances: ", distances_to_subspace)
print("Unclassified distances: ", unclassified_distances_to_subspace)

classified_as_faces = {1,2,3,4,5} # of dictionary keys

## Task 9

threshold_value = 40000000

## Task 10

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def project(M, x):
    '''
    Input:
        - M: an orthogonal matrix with row-space equal to x's domain
        - x: a Vec
    Output:
        - the projection of x into the column-space of M
    Example:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0], [0, 1], [0, 0]])
        >>> project(M, x)
        Vec({0, 1, 2},{0: 1, 1: 2, 2: 0})
        >>> M = listlist2mat([[3/5, 0], [1/5, 2/3], [1/5, 1/3]])
        >>> project(M, x)
        Vec({0, 1, 2},{0: 0.96, 1: 1.8755555555555554, 2: 1.0977777777777777})
    '''
    return projected_representation(M, x) * M

## Task 11

face_0_project = project(orthonormal_basis, face_images[0])
face_5_project = project(orthonormal_basis, face_images[5])

# Have to translate vec to list of lists for image2display function
image2display(get_listlist_from_image_vec(face_0_project))
image2display(get_listlist_from_image_vec(face_5_project))


## Task 12

unclassified_0_project = project(orthonormal_basis, unclassified_images[0])
unclassified_1_project = project(orthonormal_basis, unclassified_images[1])
unclassified_6_project = project(orthonormal_basis, unclassified_images[6])

# Have to translate vec to list of lists for image2display function
image2display(get_listlist_from_image_vec(unclassified_0_project))
image2display(get_listlist_from_image_vec(unclassified_1_project))
image2display(get_listlist_from_image_vec(unclassified_6_project))