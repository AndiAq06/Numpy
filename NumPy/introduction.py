import numpy as np

arr = np.array([1, 2, 3])
# print("Array with Rank 1 dimensions \n", arr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
# print("Array with Rank 2: \n", arr)

# Creating an array from tuple
arr = np.array((1, 2, 3))
# print('\nArray created using passed tuple:\n', arr)

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)

# Printing a range of Array
# with the use of slicing method
sliced_arr = arr[:2, ::2]
print("Array with first 2 rows and"
      " alternate columns(0 and 2):\n", sliced_arr)

# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3],
                [3, 2, 1, 0]]
print("\nElements at indices (1, 3), "
      "(1, 2), (0, 1), (3, 0):\n", Index_arr)

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[4, 3],
              [2, 1]])

# Adding 1 to every element
print("Adding 1 to every element:", a + 1)

# Subtracting 2 from each element
print("\nSubtracting 2 from each element:", b - 2)

# sum of array elements
# Performing Unary operations
print("\nSum of all array "
      "elements: ", a.sum())

# Adding two arrays
# Performing Binary operations
print("\nArray sum:\n", a + b)

# importing numpy module

# creating list
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]

# creating numpy array
sample_array = np.array([list_1,
                         list_2,
                         list_3])

print("Numpy array :")
print(sample_array)

# print shape of the array
print("Shape of the array :",
      sample_array.shape)


# iterable
iterable = (a*a for a in range(8))

arr = np.fromiter(iterable, float)

print("fromiter() array :", arr)

# Arrange
np.arange(1, 20, 2,
          dtype=np.float32)

# linspace
np.linspace(3.5, 10, 3)

# numpy ones
np.ones([4, 3],
        dtype=np.int32,
        order='f')

# numpy zeros
np.zeros([4, 3],
         dtype=np.int32,
         order='f')
