import numpy as np
def dot_vector(x, y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1
    assert x.shape[0] ==  y.shape[0] , "shape of both vectors not equal"
    z = 0
    for i in range(x.shape[0]):
        z += x[i] * y[i]
    return z

x = np.arange(2, 11)
y = np.arange(5, 14)
z = dot_vector(x, y)
print(z)
print(x.shape)

def matrix_vector_dot(x, y):
    assert len(x.shape) == 2, "must be a 2D tensor"
    assert len(y.shape) == 1, "must be a 1D tensor"
    assert x.shape[1] == y.shape[0], 'first dimension of x must be the same as the )th dimension of y'

    z = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i] += x[i, j] * y[j]
    return z

u = np.zeros(11)
print(u)
print(u[2])
m = np.array([[1, 2, 3], [3, 1 ,2]])
n = np.arange(2, 5)
o = np.array([[1, 2], [3, 1 ], [1, 1]])
print(matrix_vector_dot(m, n))
# # print(m.shape[0])
# for i in range(2):
    # print(i)
# print(m)
# print(m[1, 2])
def mmatrix_vector_dot(x, y):
    z = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        z[i] = dot_vector(x[i, :], y)
    return z

v = mmatrix_vector_dot(m, n)
print(v)

def naive_matrix_dot(x, y):
    assert len(x.shape) == 2 , "must be two dimensional tensor"
    assert len(y.shape) == 2 , "must be two dimensional tensor"
    assert x.shape[1] == y.shape[0], "first dimension of x must be the same as the 0th dimension of y"

    z = np.zeros((x.shape[0], y.shape[1]))
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            row_x = x[i, :]
            column_y = y[:, j]
            z[i, j] = dot_vector(row_x, column_y)
    return z

p = naive_matrix_dot(m, o)
print(p)


# print(np.zeros((2, 3)))
