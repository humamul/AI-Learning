import numpy as np
from sklearn.linear_model import LogisticRegression

# X = Kitne momos khaye
X = np.array([[1], [2], [5], [6]])

# y = Cold drink li ya nahi (0 = No, 1 = Yes)
y = np.array([0, 0, 1, 1])

# Model Initialize aur Train karo
model = LogisticRegression()
model.fit(X, y)

# Chalo predict karte hain ek naye customer ke liye jisne 4 momos khaye hain
naya_customer = np.array([[4]])
prediction = model.predict(naya_customer)
probability = model.predict_proba(naya_customer) # Yeh asali probability dikhayega

print(f"🔮 Prediction for 4 momos: {prediction[0]} (1 matlab lega, 0 matlab nahi)")
print(f"📊 Cold Drink na lene ki probability: {probability[0][0]} cold drink lene ki {probability[0][1]}")