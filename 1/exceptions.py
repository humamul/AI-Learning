import json

# 1. Custom Exception banana (Jaise Java mein Custom Exception banti hai)
class InvalidOrderException(Exception):
    """Custom exception when order data is corrupted or price is missing."""
    pass

# Mock Production JSON Data (Ek order corrupt hai jisme price string hai)
raw_json_data = """
[
    {"order_id": 201, "item": "Nameplate Engraving", "price": 2500},
    {"order_id": 202, "item": "Acrylic Signage", "price": "CORRUPTED_PRICE"},
    {"order_id": 203, "item": "Wooden Shield", "price": 4500}
]
"""

def process_backend_data(data_string):
    try:
        # JSON string ko Python list/dict mein parse karna
        orders = json.loads(data_string)
        
        for order in orders:
            try:
                # Type validation check
                if not isinstance(order['price'], (int, float)):
                    raise InvalidOrderException(f"Order {order['order_id']} has invalid price type!")
                
                print(f"✅ Processing Order {order['order_id']}: {order['item']} | Price: ₹{order['price']}")
                
            except InvalidOrderException as ioe:
                # Corrupted data ko catch karo taaki loop na toote (Java ka try-catch inside loop)
                print(f"🚫 LOG ERROR: {ioe} | Skipping this row safely.")
                
    except json.JSONDecodeError:
        print("🚨 CRITICAL: Root JSON format is completely invalid!")

# Execution
process_backend_data(raw_json_data)