import pandas as pd 

# Table 1: Production Floor Data (Isme duplicates aur kachra hai)
production_data = {
    'Order_ID': [501, 502, 503, 501, 504, 505, 502],
    'Client': ['Rahul', 'Amit', 'Sana', 'Rahul', 'Vikram', 'Zayan', 'Amit'],
    'Machine_Used': ['CO2 Laser', 'CNC Router', 'CO2 Laser', 'CO2 Laser', 'CNC Router', 'CO2 Laser', 'CNC Router'],
    'Raw_Material_Cost': [1500, 4500, 800, 1500, None, 3000, 4500],
    'Status': ['Completed', 'Pending', 'Completed', 'Completed', 'Completed', 'Pending', 'Pending']
}

# Table 2: Sales & Delivery Data
sales_data = {
    'Order_ID': [501, 502, 503, 504, 505],
    'City': ['Moradabad', 'Delhi', 'Noida', 'Moradabad', 'Delhi'],
    'Final_Bill_INR': [5000, 15000, 3000, 12000, 9000]
}

df_prod = pd.DataFrame(production_data)
df_sales = pd.DataFrame(sales_data)
prod_df = df_prod.drop_duplicates();
prod_df['Raw_Material_Cost'] = prod_df['Raw_Material_Cost'].fillna(prod_df['Raw_Material_Cost'].mean())
# print(prod_df)
df_master = pd.merge(prod_df,df_sales,on='Order_ID')
print(df_master)

df_master['Net_Profit'] = df_master['Final_Bill_INR'] - df_master['Raw_Material_Cost']

print(df_master)

df_master_2 = df_master[ df_master['Status'] == 'Completed']
filtered_data =df_master_2.groupby('City')['Net_Profit'].sum() #Forget added dfmaster2 again 
print(filtered_data)

pivot_data = df_master.pivot_table(index="City",columns="Machine_Used",aggfunc="sum",fill_value=0,values="Net_Profit")   
# not pd.pivot_table it should be table_name.pivot

import matplotlib.pyplot as plt
import seaborn as sns

print("🎨 LEVEL 5: VISUALIZATIONS (GRAPHS & CHARTS) 🎨")

# # --- GRAPH 1: Bar Plot (City-wise Net Profit) ---
# # Jo filtered_data aapne banaya thha (.groupby waala), usko seedha plot kar do
# plt.figure(figsize=(6, 4)) # Window ka size set karne ke liye (Width, Height)
# filtered_data.plot(kind='bar', color='skyblue', edgecolor='black')

# plt.title('City-wise Total Net Profit (Completed Orders)') # Graph ka Title
# plt.xlabel('City') # X-axis ka naam
# plt.ylabel('Net Profit in INR') # Y-axis ka naam
# plt.xticks(rotation=10) # Cities ke naam ko seedha rakhne ke liye
# plt.yticks(rotation=10) # Cities ke naam ko seedha rakhne ke liye
# plt.grid(axis='y', linestyle='--', alpha=1) # Background mein light lines
# #plt.tight_layout() # Graph ko window mein set karne ke liye
# plt.show() # Isse graph ki screen popup hogi (Bina iske graph nahi dikhega!)


# --- GRAPH 2: Seaborn Counter Plot (Machine Utilization) ---
# Yeh ginn kar batayega ki kaunsi machine kitni baar use hui
plt.figure(figsize=(6, 4))
# Ekdum warning-free aur saaf code:
sns.countplot(data=df_master, x='Machine_Used', hue='Machine_Used', palette='Set3', legend=False)

plt.title('Number of Orders per Machine')
plt.xlabel('Machine Type')
plt.ylabel('Order Count')
plt.tight_layout()
plt.show()


# --- GRAPH 3: Heatmap (Pivot Table Ka Visual Representation) ---
# Hamari matrix report ko rango (colors) mein dekhne ke liye Heatmap best hai
plt.figure(figsize=(6, 4))
# annot=True se box ke andar numbers likhe huye aayenge, cmap se color theme set hoti hai
sns.heatmap(pivot_data, annot=True, fmt=".1f", cmap="YlGnBu", cbar=True)

plt.title('Matrix Heatmap: Net Profit by City and Machine')
plt.tight_layout()
plt.show()