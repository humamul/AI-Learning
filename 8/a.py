import torch

# y = mx + b tensor should have integer only
input_A = torch.tensor([28.0])   # x Jo neuron ka input bacha tha
target = torch.tensor([0.0])     # y Actual target (Deal fail = 0)

# 2. Weight define karte hain aur 'requires_grad=True' lagate hain
# Kyunki hume isi weight ko track karna hai aur update karna hai
weight_A = torch.tensor([2.0], requires_grad=True)
bias = torch.tensor([-10.0], requires_grad=True) # Baseline bias

print(f"--- STARTING TRAINING STEP ---")
print(f"Purana Weight A: {weight_A.item()}")

# PHASE 1: FORWARD PASS (Aage badhna)
# z = (Input * Weight) + Bias
z = (input_A * weight_A) + bias  # 28 * 2 - 10 = 46

# Sigmoid Switch lagaya percentage banane ke liye
predicted_a = torch.sigmoid(z)   # Lagbhag 0.99 aayega
print(f"Predicted Output (a): {predicted_a.item():.4f}")

# C Loss calculate kiya (Mean Squared Error) -> 1/2 * (predicted - target)^2
loss = 0.5 * (predicted_a - target) ** 2
print(f"Galti (C) Kitni Aayi: {loss.item():.4f}")

# ------------------------------------
# PHASE 2: BACKPROPAGATION (Piche jaana)
# ------------------------------------
# Yeh ek line aapka poora Chain Rule automatic chala degi!
loss.backward()

# Ab check karte hain ki PyTorch ne dC/dw_A (Gradient) kya nikala
# Aapne haath se 0.274 nikala tha, dekhte hain PyTorch kya bolta hai:
gradient_A = weight_A.grad
print(f"PyTorch ka Nikala Hua Gradient: {gradient_A.item():.4f}")

# PHASE 3: WEIGHT UPDATE (Hatoda Chalana)
learning_rate = 0.1

# torch.no_grad() lagate hain taaki update karte waqt graph na bne
with torch.no_grad():
    # Naya Weight = Purana Weight - (LR * Gradient)
    weight_A -= learning_rate * gradient_A

print(f"Naya Updated Weight A: {weight_A.item():.4f}")
print(f"--------------------------------")