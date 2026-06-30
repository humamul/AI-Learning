import torch

# 1. Inputs aur Target (Normalize kiya hua data)
input_A = torch.tensor([1.5])
target = torch.tensor([0.0])  # Perfect answer hai 0.0

# 2. Weights aur Bias
weight_A = torch.tensor([-2.3], requires_grad=True)
bias = torch.tensor([-1.0], requires_grad=True)

learning_rate = 0.5
epochs = 100  # Humne 100 baar ka loop chala diya!

print("--- TRAINING LOGS (100 EPOCHS LOOP) ---")

for epoch in range(epochs): # more than one epoch 
    # --- Forward Pass ---
    z = (input_A * weight_A) + bias
    predicted_a = torch.sigmoid(z)
    
    # Loss Calculation
    loss = 0.5 * (predicted_a - target) ** 2
    
    # --- Backward Pass ---
    loss.backward()
    
    # --- Weight Update (Loop ke andar) ---
    with torch.no_grad():
        weight_A -= learning_rate * weight_A.grad
        
    # 🛑 IMP: PyTorch piche gradients ko add karta rehta hai. 
    # Isiliye har loop ke baad purane gradient ko zero karna zaroori hai, 
    # jaise hum java mein list clear karte hain.
    weight_A.grad.zero_()
    
    # Har 20 steps ke baad output print karke dekhte hain progress
    if (epoch + 1) % 20 == 0 or epoch == 0:
        print(f"Epoch {epoch+1:02d} -> Loss: {loss.item():.4f} | Output: {predicted_a.item():.4f} | Weight: {weight_A.item():.4f}")

print("---------------------------------------")
print(f"🏁 Final Trained Weight A: {weight_A.item():.4f}")