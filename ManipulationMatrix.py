import numpy as np

a= np.array((
            [1,2,3],
            [4,5,6]
            ))

print("matrix a size:", a.shape)
print(a)

# transpose matrix
print("Transpose matrix a:")
print(a.transpose())
print(np.transpose(a))
print(a.T)

# flattern array, line vector
print("flattern matrix a:")
print(a.ravel())
print(np.ravel(a))

# reshape matrix
print("reshape matrix a:")
print(a.reshape(3,2))


