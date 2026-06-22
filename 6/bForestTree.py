from sklearn.ensemble import RandomForestClassifier
import numpy as np

# --- 1. REAL-WORLD NOISY DATA PREPARATION (100 Rows) ---

X_list = []
y_list = []

# A. 60 Bade Bill Waale Log -> Sabne tip di (1), kisi ne chashma pehna, kisi ne nahi
for _ in range(20):
    X_list.append([1, 1, 0]) # Weekend, Bada Bill, Bina Chashma -> Tip = 1
    X_list.append([1, 1, 0]) # Weekend, Bada Bill, Chashma Pehna -> Tip = 1
    X_list.append([0, 1, 0]) # Weekday, Bada Bill, Bina Chashma -> Tip = 1
    y_list.extend([1, 1, 1])

# B. 40 Chhote Bill Waale Normal Log -> Kisi ne tip NAHI di (0)
# 🚨 NOISE ADDED HERE: Inme se kuch logon ko chashma pehna rahe hain jo tip nahi dete!
for _ in range(10):
    X_list.append([1, 0, 0]) # Weekend, Chhota Bill, Bina Chashma -> Tip = 0
    X_list.append([0, 0, 0]) # Weekday, Chhota Bill, Bina Chashma -> Tip = 0
    X_list.append([1, 0, 1]) # 🚨 Noise: Weekend, Chhota Bill, Chashma Pehna -> PAR TIP NAHI DI (0)
    # X_list.append([0, 0, 0]) # 🚨 Noise: Weekday, Chhota Bill, Chashma Pehna -> PAR TIP NAHI DI (0)
    y_list.extend([0, 0, 0])

# C. 🚨 HAMARA AKELA OUTLIER (101th Customer)
# Chhota bill hai, chashma pehna hai, par isne khushi mein tip DE DI (1)
X_list.append([0, 0, 1])
y_list.append(1)

# Convert to numpy arrays
X = np.array(X_list)
y = np.array(y_list)

print(f"Total Rows: {len(X)}")
print(f"Chhote bill wale total log jinhone chashma pehna hai: {sum((X[:,1]==0) & (X[:,2]==1))}")

# --- 2. RANDOM FOREST TRAINING (Khula Saand Mode - No max_depth) ---
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# --- 3. NEW CANDIDATE TEST ---
# Naya Genuine Customer: Weekday(0), Chhota Bill(0), Chashma(1)
# Isne tip nahi di hai (Asaliyat mein output 0 hona chahiye)
naya_customer = np.array([[0, 0, 1]])
prediction = rf_model.predict(naya_customer)

print("\n🌲🌲 --- Random Forest Noisy Data Result --- 🌲🌲")
print(f"🔮 Prediction for New Customer (1=Tip, 0=No): {prediction[0]}")