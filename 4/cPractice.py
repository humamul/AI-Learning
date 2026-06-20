import numpy as np
p1 = np.array([45000,4.5,12])
p2 = np.array([62000,4.8,5])

dot_product = p1 @ p2
mod_value1 = np.sqrt(np.sum(p1**2))
mod_value2 = np.sqrt(np.sum(p2**2))

ans = dot_product/(mod_value1*mod_value2)

print (ans)
if(ans>0.95): print("No Cosine Similarity")
else: print("similarity Exists")