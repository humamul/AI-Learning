import pandas as pd
import numpy as np
from io import StringIO

csv_data = """ProductID,ProductName,Category,Price,Rating,Stock
P1,Laser Engraver A,Machine,45000,4.5,12
P2,Laser Engraver B,Machine,47000,4.2,8
P3,Laser Engraver A,Machine,45000,4.5,12
P4,CNC Router X,Machine,62000,4.8,5
P5,Wood Cutter,Tool,15000,,20
P6,Laser Engraver C,Machine,46000,4.3,0
P7,Acrylic Sheet,Material,800,3.9,150
P8,CNC Router X,Machine,62000,4.8,5
P9,Metal Plate,Material,1200,,300
P10,Laser Engraver D,Machine,99000,4.6,3
"""

df = pd.read_csv(StringIO(csv_data))
machine_df = df[df['Category'] == 'Machine'].drop_duplicates()

machine_df['Z-Scale'] = (machine_df['Price']- machine_df['Price'].mean())/machine_df['Price'].std()

print(machine_df)

# Yeh exactly woh practical lesson hai jo Day 6 mein discuss kiya tha: chhote datasets mein Z-score unreliable ho sakta hai 


#Standardization FOR Good Scaling of a whole PRODUCT using price rating and stock
# cols = ['Price', 'Rating', 'Stock']

# # Z-score (Standardization): (value - mean) / std
# # ddof=0 -> population std (NumPy default style); Pandas default hota hai ddof=1
# scaled_df = (machine_df[cols] - machine_df[cols].mean()) / machine_df[cols].std(ddof=0)

# print(scaled_df)

# p1 = scaled_df.loc[machine_df['ProductID'] == 'P1'].values[0]
# p4 = scaled_df.loc[machine_df['ProductID'] == 'P4'].values[0]

# dot = p1 @ p4
# mod1 = np.sqrt(np.sum(p1**2))
# mod2 = np.sqrt(np.sum(p4**2))
# ans = dot / (mod1 * mod2)

# print("P1 z-scaled:", p1)
# print("P4 z-scaled:", p4)
# print("Cosine Similarity (Z-score):", ans)