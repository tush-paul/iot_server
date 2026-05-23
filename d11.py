# Fix default argument bug
def func(x, lst=None):
    if lst is None:
        lst = []
    lst.append(x)
    return lst
print(func(1))  # Output: [1]
