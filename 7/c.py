import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE  # Nakli chor banane ka brahmastra
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# --- STEP 1: RAW DATABASE SIMULATION ---
# Maan lo database se 10,000 rows aayin. Ek column bada hai, ek chota hai.
X, y = make_classification(
    n_samples=10000, n_features=5, weights=[0.99, 0.01], random_state=42
)

# Create a Dummy DataFrame to simulate real data
df = pd.DataFrame(X, columns=['Amount', 'Age', 'Time', 'Location_Score', 'Device_Score'])
# Intentionally making 'Amount' column very huge to show why SCALING is needed
df['Amount'] = df['Amount'] * 15000 

print("--- 📋 RAW DATA HEAD (Salary/Amount is too huge!) ---")
print(df[['Amount', 'Age']].head(2))
print("-" * 50)

# --- STEP 2: TRAIN-TEST SPLIT ---
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.20, random_state=42, stratify=y)

print(f"Original Training 1s (Chor): {sum(y_train == 1)} | 0s (Shareef): {sum(y_train == 0)}")

# --- STEP 3: FEATURE ENGINEERING (SCALING) ---
# Saare bade-chote numbers ko ek standard range mein laa rahe hain
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- STEP 4: HANDLING CLASS IMBALANCE USING SMOTE ---
# Yeh line training data mein nakli chor generate karegi taaki ratio equal ho jaye
smote = SMOTE(random_state=42,sampling_strategy=0.1)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_scaled, y_train)

print(f"SMOTE ke baad 1s (Chor): {sum(y_train_resampled == 1)} | 0s (Shareef): {sum(y_train_resampled == 0)} 🚨 (EQUALS!)")
print("-" * 50)

# --- STEP 5: MODEL TRAINING (Bina scale_pos_weight ke, kyunki SMOTE ne data balance kar diya) ---
model = XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.05, random_state=42)
model.fit(X_train_resampled, y_train_resampled)

# --- STEP 6: PRODUCTION EVALUATION ---
y_probs = model.predict_proba(X_test_scaled)[:, 1]
# Setting a practical threshold based on our knowledge
y_pred = (y_probs >= 0.4).astype(int) 

print("==================== 🧔 REAL DAY 11 METRICS REPORT ====================")
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print(f"True Negatives (TN)  : {tn} | False Positives (FP) : {fp}")
print(f"False Negatives (FN) : {fn} 🚨 | True Positives (TP)  : {tp}")
print(f"📊 ROC-AUC Score: {roc_auc_score(y_test, y_probs):.4f}")
print("=======================================================================")