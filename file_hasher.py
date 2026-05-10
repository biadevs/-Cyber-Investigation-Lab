import hashlib
from datetime import datetime

print(f"--- INVESTIGATION REPORT ---")
print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
def generate_fingerprint(filename):
    # We use SHA-256, the industry standard for security
    sha256_hash = hashlib.sha256()
    
    try:
        with open(filename, "rb") as f:
            # Read the file in small chunks (good for large industrial files!)
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        fingerprint = sha256_hash.hexdigest()
        print(f"FILE: {filename}")
        print(f"SHA-256 FINGERPRINT: {fingerprint}")
        return fingerprint

    except FileNotFoundError:
        print("Error: The evidence file was not found.")

# Run the first scan
print("--- INITIAL FINGERPRINT ---")
initial_hash = generate_fingerprint("evidence.txt")

"""
DAY 10 INVESTIGATION LOG:
Building a File Integrity Monitor. 
This is the foundation of the 'Chain of Custody' in Digital Forensics.
"""

def get_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

# 1. The "Golden Standard" (The hash we trust)
original_hash = "f821843e6b711ab1d00c1e5aa1dc6f1fb6a430ccfb570e0e937c104cc3561e60"

# 2. The Current Scan
current_hash = get_hash("evidence.txt")

print(f"Original: {original_hash}")
print(f"Current:  {current_hash}")

# 3. The Verdict
if current_hash == original_hash:
    print("\n✅ VERDICT: Evidence is AUTHENTIC. No tampering detected.")
else:
    print("\n❌ ALERT: Evidence has been MODIFIED! Integrity check failed.")
