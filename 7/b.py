import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score, roc_curve

# --- 1. DATA PREPARATION (10,000 Transactions | High Imbalance) ---
# Weights=[0.995, 0.005] ka matlab hai 99.5% shareef log (0) aur 0.5% chor (1)
X, y = make_classification(
    n_samples=10000, n_features=5, n_informative=4, n_redundant=1,
    weights=[0.995, 0.005], random_state=42
)

# Train-Test Split (80% training ke liye, 20% testing ke liye)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

# --- 2. MODEL TRAINING (Hamara Wahi Forest Tree) ---
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# --- 3. THE PROBABILITY ENGINE (Backend Probability) ---
# Predict direct 0 ya 1 nahi karega, pehle probability nikalega [0 ki, 1 ki]
# Hamein 1 (Fraud) hone ki probability chahiye, isliye [:, 1] liya
y_probs = model.predict_proba(X_test)[:, 1]


# ===================================================================
# 👦 SCENARIO A: STANDARD JUNIOR MODE (Threshold = 0.5)
# ===================================================================
y_pred_standard = (y_probs >= 0.5).astype(int)

print("==================== 👦 JUNIOR MODE (Threshold = 0.5) ====================")
tn_s, fp_s, fn_s, tp_s = confusion_matrix(y_test, y_pred_standard).ravel()
print(f"True Negatives (TN)  : {tn_s} | False Positives (FP) : {fp_s}")
print(f"False Negatives (FN) : {fn_s} 🚨 | True Positives (TP)  : {tp_s}")
print(f"🎯 Precision : {precision_score(y_test, y_pred_standard):.4f}")
print(f"📢 Recall    : {recall_score(y_test, y_pred_standard):.4f} <- (Chor chhoot gaye!)")
print(f"⚖️ F1-Score  : {f1_score(y_test, y_pred_standard):.4f}\n")


# ===================================================================
# 🧔 SCENARIO B: SENIOR SINGHAM MODE (Threshold = 0.1)
# ===================================================================
# Halka sa bhi shaq (10% probability) hua toh seedha Fraud (1) bol do!
y_pred_senior = (y_probs >= 0.1).astype(int)

print("==================== 🧔 SENIOR MODE (Threshold = 0.1) ====================")
tn_r, fp_r, fn_r, tp_r = confusion_matrix(y_test, y_pred_senior).ravel()
print(f"True Negatives (TN)  : {tn_r} | False Positives (FP) : {fp_r} <- (Normal block huye)")
print(f"False Negatives (FN) : {fn_r} 🎉 | True Positives (TP)  : {tp_r} <- (Sare chor pakde gaye!)")
print(f"🎯 Precision : {precision_score(y_test, y_pred_senior):.4f}")
print(f"📢 Recall    : {recall_score(y_test, y_pred_senior):.4f} <- (Perfect 100%!)")
print(f"⚖️ F1-Score  : {f1_score(y_test, y_pred_senior):.4f}\n")


# ===================================================================
# 📈 SCENARIO C: THE OVERALL RESULT (ROC-AUC Score)
# ===================================================================
auc_score = roc_auc_score(y_test, y_probs)
print(f"📊 Model Ka Report Card (ROC-AUC Score): {auc_score:.4f}")
print("=========================================================================\n")


# --- 4. VISUALIZING THE RESULT (ROC Curve Plotting) ---
fpr, tpr, thresholds = roc_curve(y_test, y_probs)

plt.figure(figsize=(7, 5))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC Curve (AUC = {auc_score:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Sikka Uchalna (0.5)')
plt.xlabel('False Positive Rate (Galat ko Sahi bolna)')
plt.ylabel('True Positive Rate (Sahi ko Sahi bolna)')
plt.title('Production Model Report Card (ROC Curve)')
plt.legend(loc="lower right")
plt.grid(alpha=0.3)
plt.show()