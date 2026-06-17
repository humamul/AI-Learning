import pandas as pd
import numpy as np


# 1. Ek raw kachra data banate hain (Maan lo ye database se aaya hai)
raw_data = {
    'Firm_Name': ['Artifacts Digital', 'Artifacts Digital', 'Tech Engravers', 'Pixel Cut', 'Artifacts Digital'],
    'Machine_Type': ['CO2 Laser', 'CNC Router', 'Laser Engraver', None, 'CO2 Laser'], # Ek jagah None hai
    'Price_INR': [120000, 85000, None, 45000, 120000], # Ek price missing hai
    'Orders': [12, 5, 3, 2, 12] # Duplicate rows hain isme
}

data = pd.DataFrame(raw_data) # make data in Data Frame using pandas
print(data)
clean_data = data.drop_duplicates()
print(clean_data) # dropDuplicate function will drop duplicate rows

print(clean_data.isnull().sum() ) 
# only isnull will give a dataFrame of true false in rows 
#after.sum() it gives column and number of data missing

clean_data['Machine_Type'] = clean_data['Machine_Type'].fillna('Unknown') #Pandas Immutability pandas data doesn't change Forget1 for change you need to capture it df['colName'] = 
clean_data['Price_INR'] = clean_data['Price_INR'].fillna(clean_data['Price_INR'].mean())
print(clean_data)