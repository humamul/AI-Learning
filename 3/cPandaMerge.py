import pandas as pd

# Table 1: Raw Orders Data
orders_data = {
    'Order_ID': [101, 102, 103, 104],
    'Client': ['Rahul', 'Amit', 'Sana', 'Vikram'],
    'Price_INR': [5000, 12000, 3500, 20000]
}

# Table 2: Payment Status Data
payment_data = {
    'Order_ID': [101, 102, 103, 104],
    'Advance_Paid_INR': [2000, 12000, 0, 5000],
    'Status': ['Partial', 'Fully Paid', 'Unpaid', 'Partial']
}

order_pd = pd.DataFrame(orders_data)
payment_pd = pd.DataFrame(payment_data)

merged_order_payment = pd.merge(order_pd,payment_pd,on = 'Order_ID')
print ( merged_order_payment)

merged_order_payment['Remaining_Amount'] = merged_order_payment['Price_INR'] - merged_order_payment['Advance_Paid_INR']

partial_pd = merged_order_payment[merged_order_payment['Status'] == 'Partial']
print(partial_pd)

print(partial_pd[['Client','Remaining_Amount']])