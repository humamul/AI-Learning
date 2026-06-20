import numpy as np

def process_backend_data(raw_data):
    print("--- 1. Data Cleaning Phase ---")
    # Rule 1: Agar Java/Database se koi null ya None value aayi hai, toh use pehle saaf karo
    cleaned_data = [x for x in raw_data if x is not None]
    print(f"Original Data Count: {len(raw_data)} | Cleaned Data Count: {len(cleaned_data)}")
    
    if len(cleaned_data) == 0:
        return {"status": "ERROR", "message": "No valid data to process"}

    print("\n--- 2. Core Analytics Phase ---")
    # Rule 2: Basic math metrics nikalna backend validation ke liye
    mean_val = np.mean(cleaned_data)
    std_val = np.std(cleaned_data)
    
    # Coefficient of Variance (CV) - Bhatkaav ka percentage
    cv = (std_val / mean_val * 100) if mean_val != 0 else 0
    
    metrics = {
        "mean": round(mean_val, 2),
        "std_dev": round(std_val, 2),
        "cv_percentage": round(cv, 2)
    }
    print(f"Calculated Metrics: {metrics}")

    print("\n--- 3. System Stability Alert Phase ---")
    # Rule 3: Agar CV 50% se upar hai, toh alert raise karo ki data unstable hai
    if cv > 50:
        metrics["status"] = "ALERT"
        metrics["message"] = "High Instability Detected! Data is highly volatile."
    else:
        metrics["status"] = "SUCCESS"
        metrics["message"] = "System is stable."
        
    return metrics

# ==========================================
# 🚀 LIVE TESTING (Bina Faltu Ki Math Ke)
# ==========================================

# Maan lo Java Spring Boot se hamare paas ye data aaya (jisme ek null entry bhi hai)
incoming_data = [10, 12, 11, 14, 13, None, 12, 11]

final_result = process_backend_data(incoming_data)
print("Final Output for Backend JSON Response:")
print(final_result)