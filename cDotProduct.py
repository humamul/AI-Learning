import numpy as np
print("\n--- 3. Element-wise Multiplications vs Dot Product ---")

# Maan lo hamare paas do dense vectors hain (Jaise Text Embeddings)
vec_A = np.array([1, 2, 3])
vec_B = np.array([4, 5, 6])

# A. Element-wise Multiplication (Aamne-saamne waale numbers multiply honge)
# [1*4, 2*5, 3*6] -> [4, 10, 18]
element_wise = vec_A * vec_B
print("Element-wise Multiplication:", element_wise)

# B. Asli Jadu: DOT PRODUCT (Multiply karke sabko jod dena)
# (1*4) + (2*5) + (3*6) -> 4 + 10 + 18 = 32
dot_product_1 = np.dot(vec_A, vec_B)
dot_product_2 = vec_A @ vec_B  # `@` symbol Python mein dot product ka short-cut hai

print("Dot Product (using np.dot):", dot_product_1)
print("Dot Product (using @ operator):", dot_product_2)