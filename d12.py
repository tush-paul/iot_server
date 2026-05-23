from collections import Counter

data = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(Counter(data).most_common(1)[0][0])
