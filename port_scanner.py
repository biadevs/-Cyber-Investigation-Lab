import socket

def scan_port(ip, port):
    # Create a 'socket' (the digital hand)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a 1-second timeout so we don't wait forever
    s.settimeout(1)
    
    # Try to 'connect' (the knock)
    result = s.connect_ex((ip, port))
    
    if result == 0:
        return "OPEN"
    else:
        return "CLOSED"
    s.close()
# --- 1. SET THE VARIABLES ---
target_ip = "172.17.0.1" 
ports_to_check = [22, 80, 443, 3306, 8080]

# --- 2. PRINT THE HEADER (Note: This is its own line now!) ---
print(f"--- Scanning Target: {target_ip} ---")

# --- 3. RUN THE LOOP ---
for port in ports_to_check:
    status = scan_port(target_ip, port)
    print(f"Port {port}: {status}")
