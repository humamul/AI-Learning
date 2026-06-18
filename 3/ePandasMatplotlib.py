import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

# ==============================================================================
# 📋 RAW DATA BLOCK (Simulating loading 'sales_records.csv' from Kaggle)
# ==============================================================================
csv_data = """Order_ID,Client_Name,Region,Product_Type,Purchase_INR,Status
1001,Amit,Delhi,CO2 Laser,240000,Delivered
1002,Rahul,Moradabad,CNC Router,450000,Pending
1003,Sana,Noida,CO2 Laser,240000,Delivered
1004,Amit,Delhi,CO2 Laser,240000,Pending
1005,Vikram,Moradabad,Metal Engraving,180000,Delivered
1006,Rahul,Moradabad,CNC Router,450000,Delivered
1007,Zayan,Noida,Metal Engraving,None,Pending
1001,Amit,Delhi,CO2 Laser,240000,Delivered
"""
# Loading the simulated CSV into a DataFrame
df_sale = pd.read_csv(io.StringIO(csv_data))
# ==============================================================================

# 🔥 HUMAM'S SELF-CODING CHALLENGE STARTS HERE! 🔥
# Bina pichla code dekhe, line-by-line khud type karo.

# Task 1: Cleaning & Basic Checks
# (Duplicates hatao, missing values check karo, 'Purchase_INR' column mein average fill karo)

# Task 2: Advanced Reporting (Pivot Table)
# (Create a Matrix Report: Rows='Region', Columns='Product_Type', Values='Purchase_INR', aggfunc='sum', fill_value=0)

# Task 3: Visualizations (Create 2 Charts)
# Graph A: A simple Bar Chart (kind='bar') showing Region-wise Total Purchase_INR.
# Graph B: A simple Count Plot (sns.countplot) showing which Status (Delivered/Pending) is more frequent.

# Important: Dont forget to use plt.show() to see the graphs.
#df_sale = pd.DataFrame(df_sales)
d_sale = df_sale.drop_duplicates()

#print(d_sale)

d_sale['Purchase_INR'] = d_sale['Purchase_INR'].fillna(d_sale['Purchase_INR'].mean())
x = d_sale.groupby('Region')['Purchase_INR'].sum()
print(x)

pivot_sale=d_sale.pivot_table(index='Region',columns='Product_Type',values='Purchase_INR',aggfunc='sum', fill_value=0)

print(pivot_sale)

plt.figure(figsize=(6,4))
x.plot(kind='bar',color='green',edgecolor='black')
plt.title('Region Wise Sales')
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(rotation=10)
plt.ticklabel_format(style='plain',axis='y') #forget 1 whole line should be in mind

plt.figure(figsize=(6,4))
sns.countplot(data=d_sale,x='Status',hue='Status') #Forget 4

plt.figure(figsize=(6,4))
sns.heatmap(pivot_sale,annot=True, fmt=".1f") #forget 3
plt.xlabel('Machine')
plt.ylabel('Region')
plt.tight_layout()  #forget 2 
plt.show()