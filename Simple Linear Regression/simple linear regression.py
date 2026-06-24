from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

#data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])

#train model
model = LinearRegression()
model.fit(X, y)

#prediction
new_value = np.array([[6]])
prediction = model.predict(new_value)

print("Prediction for x = 6:", prediction[0])
print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)

#graph
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.title("Simple Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")

#show graph
plt.show()

input("Press Enter to exit...")