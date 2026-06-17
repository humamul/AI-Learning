import time 
import numpy as np
print("\n--- 2. Speed Benchmark: Loop vs NumPy ---")

size = 10  # 10 Lakh elements
python_list1 = list(range(size))
python_list2 = list(range(size))
print(python_list1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numpy_arr1 = np.arange(size)
numpy_arr2 = np.arange(size)
print(numpy_arr1) #[0 1 2 3 4 5 6 7 8 9] without comas

# A. Pure Python Loop Se Addition
start_time = time.time()
python_result = [x + y for x, y in zip(python_list1, python_list2)]
python_duration = time.time() - start_time
print(f"⏱️ Pure Python Loop took: {python_duration:.6f} seconds : {python_result}")

# B. NumPy Vectorized Addition (Bina kisi loop ke, direct operation!)
start_time = time.time()
numpy_result = numpy_arr1 + numpy_arr2
numpy_duration = time.time() - start_time
print(f"⏱️ NumPy Vectorization took: {numpy_duration:.6f} seconds : {numpy_result}")

print(f"🚀 NumPy is {python_duration / numpy_duration:.2f}x FASTER!")