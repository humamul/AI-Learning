from sklearn.tree import DecisionTreeClassifier, export_text
import numpy as np

# --- 1. DATA PREPARATION (3 Features: [Weekend, Bill > 500, Chashma]) ---
X = np.array([
    # 6 shareef log (Bade Bill waale) -> Kisi ne chashma pehna tha, kisi ne nahi, par sabne tip di
    [1, 1, 0], [1, 1, 1], [1, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 0],
    
    # 4 log (Chhote Bill waale) -> Kisi ne chashma nahi pehna tha, tip nahi di
    [1, 0, 0], [1, 0, 0], [0, 0, 0], [0, 0, 0],
    
    # 🚨 11th Customer: OUTLIER (Weekday=0, Chhota Bill=0, par Chashma PEHNA THA=1) -> Tip DE DI (1)
    [0, 0, 1] 
])

# Target (y): Pehle 6 ne di (1), agle 4 ne nahi di (0), outlier ne di (1)
y = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1])

# --- 2. MODEL TRAINING (No max_depth = Khula Saand Mode) ---
model = DecisionTreeClassifier(criterion='gini', random_state=42 , max_depth=2)
model.fit(X, y)

# --- 3. ASALIAT CHECK IN TERMINAL ---
# Ab export_text mein teenon features ke naam daalenge
tree_rules = export_text(model, feature_names=['Weekend', 'Bill_GT_500', 'Chashma'])
print("🌲 --- Actual Overfitted Decision Tree --- 🌲")
print(tree_rules)

# --- 4. NEW CANDIDATE TEST (The Crash) ---
# Naya Genuine Customer: Weekday (0), Chhota Bill (0), par bechara chashma pehnta hai (1)
# Asaliyat mein isne tip nahi di, par machine ne kya ratta mara hai dekho:
naya_customer = np.array([[0, 0, 1]])
prediction = model.predict(naya_customer)

print("\n--- Prediction Result ---")
print(f"🔮 Naye customer ki prediction (1=Tip, 0=No): {prediction[0]}")

# Day 9: Step-by-Step Decision Tree Calculation
# Shuruat Ka Data (Initial State)
# Pure dhabe mein total 11 log hain:

# Tip dene waale (1) = 7 log

# Tip NAHI dene waale (0) = 4 log

# Initial Gini Formula: 1 - (7/11)^2 - (4/11)^2

# 1 - (0.636)^2 - (0.363)^2

# 1 - 0.404 - 0.131

# Initial Gini = 0.465

# TEST 1: Sawaal - "Kya Bill > 500 Hai?"
# Agar machine is sawaal par data ko baanti hai, toh 11 log do hisson mein tootenge:

# Scenario A: Bill > 500 (Bade Bill Waale = 6 Log)
# Yeh 6 ke 6 log shareef hain aur sabne tip di hai (yaani 6 log 'Tip=1' aur 0 log 'Tip=0').

# Gini Left = 1 - (6/6)^2 - (0/6)^2

# 1 - 1 - 0 = 0 (Ekdum Pure Group)

# Scenario B: Bill <= 500 (Chhote Bill Waale = 5 Log Bache)
# In 5 logon mein se 4 normal logon ne tip nahi di (0) aur 1 hamare khush wale outlier ne tip de di (1).

# Gini Right = 1 - (1/5)^2 - (4/5)^2

# 1 - 0.04 - 0.64 = 0.32

# Weighted Gini (Bill) Ka Calculation:
# Weighted Gini = (6/11 * Gini Left) + (5/11 * Gini Right)

# (6/11 * 0) + (5/11 * 0.32)

# 0 + (0.545 * 0.32) = 0.174

# Final Gini Gain (Bill):
# Gini Gain = Initial Gini - Weighted Gini

# 0.465 - 0.174 = 0.291

# TEST 2: Sawaal - "Kya Chashma Pehna Hai?"
# Data mein total 3 logon ne chashma pehna hai (2 bade bill waale + 1 outlier). Baaki 8 logon ne chashma nahi pehna.

# Scenario A: Chashma = 1 (Chashma Pehna Hai = 3 Log)
# Teeno ne tip di hai (3 log 'Tip=1' aur 0 log 'Tip=0').

# Gini Left = 1 - (3/3)^2 - (0/3)^2 = 0 (Pure)

# Scenario B: Chashma = 0 (Chashma Nahi Pehna = 8 Log)
# In 8 mein se 4 bade bill walon ne tip di hai (1) aur 4 chhote bill walon ne tip nahi di (0). Data ekdum mix hai.

# Gini Right = 1 - (4/8)^2 - (4/8)^2

# 1 - 0.25 - 0.25 = 0.50 (Poora Kachra)

# Weighted Gini (Chashma) Ka Calculation:
# Weighted Gini = (3/11 * 0) + (8/11 * 0.50)

# 0 + (0.727 * 0.50) = 0.363

# Final Gini Gain (Chashma):
# Gini Gain = Initial Gini - Weighted Gini

# 0.465 - 0.363 = 0.102

# TEST 3: Sawaal - "Kya Weekend Thaa?"
# Total 7 log weekend par aaye the aur 4 log weekdays par.

# Scenario A: Weekend = 1 (Weekend Thaa = 7 Log)
# 5 ne tip di, 2 ne nahi di.

# Gini Left = 1 - (5/7)^2 - (2/7)^2 = 1 - 0.51 - 0.08 = 0.41

# Scenario B: Weekend = 0 (Weekday Thaa = 4 Log)
# 2 ne tip di, 2 ne nahi di.

# Gini Right = 1 - (2/4)^2 - (2/4)^2 = 1 - 0.25 - 0.25 = 0.50

# Weighted Gini (Weekend) Ka Calculation:
# Weighted Gini = (7/11 * 0.41) + (4/11 * 0.50)

# 0.26 + 0.18 = 0.44

# Final Gini Gain (Weekend):
# Gini Gain = Initial Gini - Weighted Gini

# 0.465 - 0.44 = 0.025

# 🏆 Final Result Tree Decision
# Gini Gain (Bill > 500) = 0.291 -> WINNER! 🌲

# Gini Gain (Chashma) = 0.102 -> Rejected

# Gini Gain (Weekend) = 0.025 -> Rejected