data = ["apple", "banana", "apple", "orange", "banana", "apple"]
a = []
for i in data:
    if i not in a:
        a.append(i)
print(a)