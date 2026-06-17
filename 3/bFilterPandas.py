import pandas as pd
import numpy as np

server_logs = {
    'Timestamp': ['10:00', '10:01', '10:02', '10:03', '10:04', '10:05', '10:06', '10:07', '10:08', '10:09'],
    'Service': ['Spring_Boot', 'Python_AI', 'Spring_Boot', 'Spring_Boot', 'Python_AI', 'Python_AI', 'Spring_Boot', 'Database', 'Database', 'Python_AI'],
    'Endpoint': ['/login', '/predict', '/getOrders', '/createBill', '/predict', '/embed', '/login', '/queryUser', '/updateStock', '/predict'],
    'Response_Time_MS': [45, 1200, 80, 150, 950, 450, 50, 12, 18, 1400],
    'Status_Code': [200, 200, 200, 500, 200, 200, 200, 200, 500, 200]
}

df_logs = pd.DataFrame(server_logs)
print("--- Asli Server Logs ---")
#print(df_logs)

time_taking_apis = df_logs['Response_Time_MS'] > 500
print(time_taking_apis) #giving only index and true false for every data

time_taking_apis_df = df_logs[df_logs['Response_Time_MS'] > 500] #after adding another layer of df_logs[] it filters out 
print(time_taking_apis_df)

failed_apis = df_logs[df_logs['Status_Code'] == 500]
print(failed_apis)

group_by_task = df_logs.groupby('Service')['Response_Time_MS'].sum() #['Response_Time_MS'].sum() iske bina address ayga aur responseTime ko bina df_data ko dobara use kiye ushi pe bulana h aur sum krna h 
print(group_by_task)