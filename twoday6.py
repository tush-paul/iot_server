import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([10, 20, 30, 40, 100])

model = LinearRegression()

model.fit(X, y)

print(model.predict(np.array([[6]])))
