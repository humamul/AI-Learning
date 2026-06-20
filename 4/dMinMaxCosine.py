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

# Min-Max scaling Forget 1 : u need cols then min max of cols to get the scaled values for each column u wanted
cols = ['Price', 'Rating', 'Stock']
scaled_df = (machine_df[cols] - machine_df[cols].min()) / (machine_df[cols].max() - machine_df[cols].min())

print(scaled_df)

p1 = scaled_df.loc[machine_df['ProductID'] == 'P1'].values[0]
p4 = scaled_df.loc[machine_df['ProductID'] == 'P4'].values[0]

dot = p1 @ p4
mod1 = np.sqrt(np.sum(p1**2))
mod2 = np.sqrt(np.sum(p4**2))
ans = dot / (mod1 * mod2)

print("P1 scaled:", p1)
print("P4 scaled:", p4)
print("Cosine Similarity:", ans)


#FOR BETTER UNDERSTANDING
# print(machine_df['ProductID'] == 'P1')        # Step 1: True/False list
print(scaled_df.loc[machine_df['ProductID'] == 'P1'])
# Step 2: filtered row (table form) scaled_df ke loc ke hisab se values

print(scaled_df.loc[machine_df['ProductID'] == 'P1'].values)   # Step 3: array form
print(scaled_df.loc[machine_df['ProductID'] == 'P1'].values[0])  # Step 4: final plain array
# ye upar ke 4 print gives us insight of p1 without .values()
# it is in table form .values gives nested array so we take out first 1 using[0]