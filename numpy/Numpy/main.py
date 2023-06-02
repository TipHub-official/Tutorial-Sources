import numpy as np

# my_list = [1, 2, 3, 4]
# my_array1 = np.array([1, 2, 3, 4])
# print(my_list)
# print(my_array1)
# print(type(my_list))
# print(type(my_array1))

# my_array1 = np.array([1, 2, 3, 4])
# my_array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(my_array1)
# print(my_array2)
# print(my_array1[1])
# print(my_array2[0][1])

# my_list = [1, 2, 3]
# data = ['ali', 2, 4.3]
# my_array = np.array(my_list)
# data_array = np.array(data)
# print(my_array)
# print(data_array)

# my_array = np.array([i for i in range(10)])
# my_array2 = np.array([range(i, i+2) for i in [1, 3, 5]])
# print(my_array)
# print(my_array2)

# my_array3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(my_array3)
# print(my_array3[0][-1][0])

# zeros = np.zeros(5)
# ones = np.ones(5)
# ones2 = np.zeros((3, 3), dtype=int)
# print(zeros)
# print(ones)
# print(ones2)

# my_array = np.full((2, 3), 4.5)
# print(my_array)

# my_array = np.empty((4, 4), dtype=int)
# print(my_array)

# my_array1 = np.arange(5)
# my_array2 = np.arange(1, 11, 3)
# print(my_array1)
# print(my_array2)

# my_array = np.linspace(0, 10, 5)
# print(my_array)

# -----------------------------------------------------

# my_array = np.random.random(4)
# print(my_array)

# my_array = np.random.randint(0, 10, (6, 5))
# print(my_array)
# print(my_array.ndim)
# print(my_array.size)
# print(my_array.shape)
# print(my_array.dtype)

# my_array = np.arange(1, 11)
# print(my_array)
# print(my_array[1:5])
# print(my_array[3:])
# x = np.reshape(my_array, (2, 5))
# print(x)

# my_array = np.random.randint(1, 10, (4, 5))
# print(my_array)
# # print(my_array[:2, :2])
# # print(my_array[:2, ::2])
# # print(my_array[::2, :2])
# # print(my_array[my_array > 5])
# more_than_three = (my_array >= 3)
# print(my_array[more_than_three])

# -----------------------------------------------------

# x = np.array([2, 5, 6, 1, 4, 3])
# print(np.sort(x))

# a1 = np.array([[1, 1],
#                [2, 2]])
# a2 = np.array([[3, 3],
#                [4, 4]])
# # x = np.vstack((a1, a2))
# y = np.hstack((a1, a2))
# # print(x)
# print(y)
#
# a1 = np.array([[1, 1], [2, 2]])
# a2 = np.array([[3, 3], [4, 4]])
# print(np.concatenate((a1, a2), axis=1))

# x = np.arange(1, 37).reshape(6, 6)
# print(x)
# y = np.vsplit(x, 2)
# print(y)

# x = np.array([[1, 1], [2, 2]])
# # print(x.sum(axis=1))
# print(x * 2)

# x = np.random.randint(1, 21, (4, 5))
# print(x)
# # print(x.max())
# # print(x.min())
# print(x.sum(axis=1))

