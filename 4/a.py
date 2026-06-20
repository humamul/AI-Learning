import numpy as np
import matplotlib.pyplot as plt

arr = [1, 2, 3, 4, 4, 4, 4, 6,14444]
mean_val = np.mean(arr)
std_val = np.std(arr)

print("Variance:", np.var(arr))
print("Std Deviation:", std_val)
print("Mean:", mean_val)

coefficient_of_variance = std_val / mean_val * 100
print("Coefficient of Variance:", coefficient_of_variance)

# Perfect Bell Curve ke liye data points (Engine + Manager)
x_axis = np.linspace(mean_val - 4 * std_val, mean_val + 4 * std_val, 1000)
y_axis = (1 / (std_val * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_axis - mean_val) / std_val) ** 2)

# Deewaron ke mathematical points
d1_low, d1_high = mean_val - std_val, mean_val + std_val
d2_low, d2_high = mean_val - 2 * std_val, mean_val + 2 * std_val
d3_low, d3_high = mean_val - 3 * std_val, mean_val + 3 * std_val

# ==========================================
# 📊 PLOTTING GRAPH (Asali Jalwa)
# ==========================================

# 1. Main Bell Curve line draw karein
plt.plot(x_axis, y_axis, color="black", linewidth=2.5, label="Perfect Bell Curve (PDF)")

# 2. Bilkul center mein Mean ki line (Pahaad ki choti)
plt.axvline(mean_val, color="red", linestyle="dashed", linewidth=2, label=f"Mean ({mean_val})")

# 3. Pehli Deewar (68% Data) - Green Color
plt.axvline(d1_low, color="green", linestyle="dotted", linewidth=1.5, label="1st Wall (68%)")
plt.axvline(d1_high, color="green", linestyle="dotted", linewidth=1.5)

# 4. Doosri Deewar (95% Data) - Blue Color
plt.axvline(d2_low, color="blue", linestyle="dotted", linewidth=1.5, label="2nd Wall (95%)")
plt.axvline(d2_high, color="blue", linestyle="dotted", linewidth=1.5)

# 5. Teesri Deewar (99.7% Data) - Orange Color
plt.axvline(d3_low, color="orange", linestyle="dotted", linewidth=1.5, label="3rd Wall (99.7%)")
plt.axvline(d3_high, color="orange", linestyle="dotted", linewidth=1.5)

# 6. Graph ko sundar aur readable banane ke liye settings
plt.title("Normal Distribution & Empirical Rule (Humam's Blueprint)", fontsize=14, fontweight='bold')
plt.xlabel("Data Values (x_axis)", fontsize=12)
plt.ylabel("Probability Density (y_axis)", fontsize=12)
plt.legend(loc="upper right") # Labels ko box mein dikhane ke liye
plt.grid(alpha=0.3) # Background mein halki lines

# 7. Screen par graph pop-up karne ka final command
plt.show()
