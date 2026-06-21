from sklearn.linear_model import LinearRegression
import numpy as np

# Experience vs Salary
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Experience
print(X) # conversion of [1 2 3 4 5] -> [[1] [2] [3] [4] [5]]
y = np.array([30000, 35000, 45000, 50000, 60000])  # Salary

model = LinearRegression()
model.fit(X, y)

print("Slope (m):", model.coef_)
print("Intercept (c):", model.intercept_)
print("Predicted salary for 6 yrs exp:", model.predict([[6]]))