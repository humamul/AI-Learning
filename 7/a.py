import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score

# --- 1. REALISTIC DATA ENGINE (Imbalance + High Separation) ---
X, y = make_classification(
    n_samples=100000, n_features=20, n_informative=18, n_redundant=2,
    weights=[0.995, 0.005], class_sep=2.2, random_state=42  
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

# --- 2. SENIOR TUNED MODEL (Lever 1 & 3: Better Generalization + High Penalty) ---
model = XGBClassifier(
    n_estimators=500,         # Trees badhaye complex pattern pakadne ko
    max_depth=4,              # Shallower trees = overfitting control
    scale_pos_weight=350,     # Lever 1: Fraud class ko 350 guna penalty!
    learning_rate=0.02,
    min_child_weight=1,       # Fraud samples kam hain, 1 rakhna zaroori
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
model.fit(X_train, y_train)

# --- 3. PROBABILITY ENGINE ---
y_probs = model.predict_proba(X_test)[:, 1]

print("==================== 🎛️ SYSTEMATIC THRESHOLD TUNING ====================")
print(f"📊 Model Ka Report Card (ROC-AUC Score): {roc_auc_score(y_test, y_probs):.4f} 🔥\n")
print(f"{'Threshold':<10} | {'Recall':<8} | {'Precision':<10} | {'FP (False Alarm)':<16} | {'FN (Missed)':<12}")
print("-" * 65)

# --- 4. THE AUTOMATED EXECUTIVE LOOP (Lever 2 Testing) ---
# Alag-alag thresholds par system ka checking system
for thresh in [0.5, 0.3, 0.1, 0.05, 0.02, 0.01, 0.005, 0.001]:
    y_pred = (y_probs >= thresh).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    
    r = tp / (tp + fn) if (tp + fn) > 0 else 0
    p = tp / (tp + fp) if (tp + fp) > 0 else 0
    
    print(f"{thresh:<10.3f} | {r:<8.3f} | {p:<10.3f} | {fp:<16} | {fn:<12}")

print("=========================================================================")