import numpy as np
import time

print("--- 1. Vector aur Matrix Creation ---")

# 1D Array -> Isiko Data Science/AI mein "Vector" bolte hain (Jaise Embeddings)
embedding_vector = np.array([0.12, -0.45, 0.89, 0.34])
print("Embedding Vector:\n", embedding_vector)
print("Vector Ki Shape:", embedding_vector.shape) # Output: (4,) -> 4 elements ka 1D vector

print("-" * 40)

# 2D Array -> Isiko bolte hain "Matrix" (Rows x Columns)
# Maan lo Artifacts Digital Engravers ke 3 orders hain aur har order ke 2 features hain [Price, MachineTypeID]
orders_matrix = np.array([
    [15000, 1],  # Row 0
    [8500,  1],  # Row 1
    [60000, 2]   # Row 2
])
print("Orders Matrix:\n", orders_matrix)
print("Matrix Ki Shape:", orders_matrix.shape) # Output: (3, 2) -> 3 Rows, 2 Columns