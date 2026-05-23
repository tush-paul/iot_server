import numpy as np
from sklearn.linear_model import LinearRegression

# Input data
X = np.array([[1], [2], [3], [4]])
y = np.array([10, 20, 30, 40])

# Model
model = LinearRegression()

# Train
model.fit(X, y)

# Predict
pred = model.predict([[5]])

print(pred)
