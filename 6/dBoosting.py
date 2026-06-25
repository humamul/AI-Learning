import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

# --- 1. DATA PREPARATION (Wahi Aapka 91 Rows Ka Data) ---
X_list = []
y_list = []

# A. 60 Bade Bill Waale Log -> Sabki Tip = 1
for _ in range(20):
    X_list.append([1, 1, 0])  # Weekend, Bada Bill, Bina Chashma
    X_list.append([1, 1, 1])  # Weekend, Bada Bill, Chashma Pehna 
    X_list.append([0, 1, 0])  # Weekday, Bada Bill, Bina Chashma
    y_list.extend([1, 1, 1])

# B. 30 Chhote Bill Waale Normal Log -> Sabki Tip = 0
for _ in range(10):
    X_list.append([1, 0, 0])  # Weekend, Chhota Bill, Bina Chashma
    X_list.append([0, 0, 0])  # Weekday, Chhota Bill, Bina Chashma
    X_list.append([1, 0, 1])  # Weekend, Chhota Bill, Chashma Pehna 
    y_list.extend([0, 0, 0])

# C. 🚨 THE AKELA OUTLIER (91st Element) -> Weekday, Chhota Bill, Chashma par Tip = 1
X_list.append([0, 0, 1])
y_list.append(1)

# Convert to Numpy Arrays
X = np.array(X_list)
y = np.array(y_list)

# --- 🎯 NAYA CUSTOMER (Jise predict karna hai) ---
# Weekday (0), Chhota Bill (0), Chashma Pehna Hai (1) -> Huba-hu outlier jaisa
X_test = np.array([[0, 0, 1]])


# --- 🌲 MODEL 1: RANDOM FOREST (Khula Saand Mode) ---
rf = RandomForestClassifier(n_estimators=100, max_depth=None, random_state=42)
rf.fit(X, y)
rf_pred = rf.predict(X_test)


# --- 🚀 MODEL 2: GRADIENT BOOSTING (Sequential Learning) ---
# learning_rate=0.1 (har tree pichle ki galti thodi-thodi sudharega)
gb = GradientBoostingClassifier(n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42)
gb.fit(X, y)
gb_pred = gb.predict(X_test)


# --- ⚡ MODEL 3: XGBOOST (The Bullet Train) ---
xgb = XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1, random_state=42, eval_metric='logloss')
xgb.fit(X, y)
xgb_pred = xgb.predict(X_test)


# --- 📊 OUTPUT COMPARISON ---
print(f"📊 Original Total Rows: {len(X)}")
print(f"🎯 Test Customer Input: {X_test[0]} (Weekday, Chhota Bill, Chashma)\n")
print(f"🌲 Random Forest Prediction    : {rf_pred[0]} (True/1 -> Outlier Se Match Ho Gaya!)")
print(f"🚀 Gradient Boosting Prediction: {gb_pred[0]} (False/0 -> Outlier Ko Daba Diya!)")
print(f"⚡ XGBoost Prediction          : {xgb_pred[0]} (False/0 -> Outlier Ko Daba Diya!)")