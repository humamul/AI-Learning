import sys

# Raw Mock Data: Artifacts Digital Engravers ke orders
raw_orders = [
    {"order_id": 101, "price": 15000, "machine": "Laser CO2", "status": "ACTIVE"},
    {"order_id": 102, "price": -500,  "machine": "CNC Router", "status": "ACTIVE"},     # 🚫 Invalid Price
    {"order_id": 103, "price": 45000, "machine": "Fiber Laser", "status": "SUSPENDED"}, # 🚫 Suspended
    {"order_id": 104, "price": 8500,  "machine": "Laser CO2", "status": "ACTIVE"},
    {"order_id": 105, "price": 60000, "machine": "CNC Router", "status": "ACTIVE"}
]

# Hardware Batch Configurations (Nested Loop ke liye matrix)
machine_batches = [["Laser CO2", "Fiber Laser"], ["CNC Router"]]

task1 =[ order['machine'] for order in raw_orders if order['price'] >20000]
for i in task1:
    print (f"machine worth more than 20000: {i}")

task2 = [
    f"ID: {order['order_id']}: STATUS APPROVED"
    if order['status'] == 'ACTIVE'
    else f"ID: {order['order_id']}: STATUS DECLINED"
    for order in raw_orders
]

for i in task2:
    print(i)

task3 = (order['order_id'] for order in raw_orders if "laser" not in order['machine'].lower() ) #string check exist in another string
print (next(task3,"Daym")) 
print (next(task3,"Daym")) 
print (next(task3,"Daym")) # default value for no error while fetching
print (next(task3,"Daym")) 

task4 = tuple(order['order_id'] for order in raw_orders if "laser" in order['machine'].lower() ) #string check exist in another string
for i in task4:
    print(i)