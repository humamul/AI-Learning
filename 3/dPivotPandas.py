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
print(prod_df)
df_master = pd.merge(prod_df,df_sales,on='Order_ID')
print(df_master)

df_master['Net_Profit'] = df_master['Final_Bill_INR'] - df_master['Raw_Material_Cost']

print(df_master)

df_master_2 = df_master[ df_master['Status'] == 'Completed']
filtered_data =df_master_2.groupby('City')['Net_Profit'].sum() #Forget added dfmaster2 again 
print(filtered_data)

pivot_data = df_master.pivot_table(index="City",columns="Machine_Used",aggfunc="sum",fill_value=0,values="Net_Profit")   
# not pd.pivot_table it should be table_name.pivot