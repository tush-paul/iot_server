# lis = ["apple", "banana", "apricot", "blueberry"]
# d = {}
# for i in lis:
#     if i[0] not in d.keys():
#         d[i[0]] = [i]
#     else:
#         d[i[0]].append(i)
# print(d)
from collections import defaultdict

# Example 1: grouping
words = ["apple", "banana", "apricot", "blueberry"]

d = defaultdict(list)

for w in words:
    d[w[0]].append(w)

print(d)