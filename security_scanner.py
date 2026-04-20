# Simple Forensic Log Scanner
logs = [
    "User login: admin",
    "User login: guest",
    "ALERT: Unauthorized access attempt from IP 192.168.1.50",
    "User login: user1",
    "WARNING: Multiple failed logins from IP 10.0.0.15",
    "CRITICAL: System kernel modification detected!" 
]

print("--- Starting Security Scan ---")
for entry in logs:
    if "ALERT" in entry or "WARNING" or "CRITICAL" in entry:
        print(f"[!] Security Threat Found: {entry}")
print("--- Scan Complete ---")
