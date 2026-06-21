import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Hamare wahi 3 real customers (Data Points)
# X = Momos ki quantity (Iska shape hamesha 2D column matrix hona chahiye)
X = np.array([[4], 
              [2], 
              [6]])

# y = Asali Bill (Jo hume pata hai ground truth hai)
y = np.array([50, 30, 70])

print("--- Training Shuru Karte Hain ---")

# 2. Scikit-Learn ka Linear Regression engine initialize karo
# Iske andar backend par wahi Gradient Descent / OLS algorithm chalta hai
model = LinearRegression()

# 3. Model ko data 'Fit' karo (Yaani yeh wahi Roz Raat ki learning cycle chalayega)
model.fit(X, y)

print("--- Training Khatam! ---")
print("")

# 4. Ab nikaalte hain backend se weight (m) aur bias (c) ki trained values
trained_m = model.coef_[0]
trained_c = model.intercept_

print(f"🤖 Machine ne seekha hua Momos ka Rate (m): {trained_m:.2f} Rs/momo")
print(f"🤖 Machine ne seekha hua Fixed Rent (c)   : {trained_c:.2f} Rs")
print("-" * 40)
print("🎯 Dekha? Machine ne wahi dhoond liya jo hamara target tha: m=10, c=10!")
print("-" * 40)

# 5. TEST TIME: Ab dukan par ek naya customer aaya jisne 10 momos khaye!
# Ab iska asli bill hamare paas nahi hai, model se predict karwate hain
naya_customer_momos = np.array([[10]])
predicted_bill = model.predict(naya_customer_momos)

print(f"🔮 Prediction for 10 Momos: Rs. {predicted_bill[0]:.2f}")
print("Formula match karo: (10 momos * 10 rate) + 10 rent = 110 Rs. Ekdum Perfect!")