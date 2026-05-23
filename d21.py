import time
import numpy as np

SIZE = 10_000_000

# ---------------------------
# Python List
# ---------------------------
list1 = list(range(SIZE))
list2 = list(range(SIZE))

start = time.time()

result = []
for i in range(SIZE):
    result.append(list1[i] + list2[i])

end = time.time()

print(f"Python List Time: {end - start:.4f} seconds")


# ---------------------------
# NumPy Array
# ---------------------------
arr1 = np.arange(SIZE)
arr2 = np.arange(SIZE)

start = time.time()

result = arr1 + arr2

end = time.time()

print(f"NumPy Array Time: {end - start:.4f} seconds")