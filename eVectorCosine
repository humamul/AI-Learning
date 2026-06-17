import numpy as np

print("=============================================")
print("🚀 HUMAM BHAI KA VECTOR & MATHS TESTBENCH 🚀")
print("=============================================\n")

# --- 1. BROADCASTING (Ek scalar number sabpe apply) ---
print("--- 1. Broadcasting Ka Jadu ---")
vec = np.array([1, 2, 3, 4, 5])
print("Original Vector:", vec)

# Bina kisi loop ke har element mein 5 plus ho jayega
vec_plus_5 = vec + 5 
print("Vector + 5 (Broadcasting):", vec_plus_5) # [6 7 8 9 10]

# Har element ko 10 se multiply karna ho
vec_mult_10 = vec * 10
print("Vector * 10 (Broadcasting):", vec_mult_10) # [10 20 30 40 50]\n")


# --- 2. COSINE SIMILARITY FROM SCRATCH ---
print("--- 2. Cosine Similarity (AI Search Engine) ---")

# Maan lo do text embeddings hain (Numbers paas-paas hain matlab context same hai)
vec_A = np.array([3, 4, 0])  # Maan lo ye "Java" ka vector hai
vec_B = np.array([3, 5, 0])  # Maan lo ye "Spring Boot" ka vector hai

# Sahi formula jo aapne pakda: (A @ B) / (A_length * B_length)
dot_product = vec_A @ vec_B
print(np.sum(vec_A**2))
# Length (Norm) nikaalne ka formula
length_A = np.sqrt(np.sum(vec_A**2))
length_B = np.sqrt(np.sum(vec_B**2))

# Cosine Score
cosine_score = dot_product / (length_A * length_B)

print("Vector A (Java):", vec_A)
print("Vector B (Spring Boot):", vec_B)
print(f"Dono ka Dot Product (@): {dot_product}")
print(f"Vector A ki length: {length_A:.4f}")
print(f"Vector B ki length: {length_B:.4f}")
print(f"🔥 Final Similarity Score (0 se 1): {cosine_score:.4f}")

if cosine_score > 0.95:
    print("🎯 Result: Dono vectors ekdum similar hain! Kaam ho gaya!")
else:
    print("❌ Result: Vectors alg hain.")