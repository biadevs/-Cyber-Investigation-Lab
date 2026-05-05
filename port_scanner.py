import socket

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2) # Give it a bit more time to talk back
        result = s.connect_ex((ip, port))
        
        if result == 0:
            # TRY TO GRAB THE BANNER
            try:
                # Send a small request or just wait for the greeting
                s.send(b'Hello\r\n')
                banner = s.recv(1024).decode().strip()
                return f"OPEN (Banner: {banner})"
            except:
                return "OPEN (No banner found)"
        else:
            return "CLOSED"
        s.close()
    except Exception as e:
        return f"ERROR: {e}"
    

# --- 1. SET THE VARIABLES ---
target_ip = "172.17.0.1" 
ports_to_check = [22, 80, 443, 3306, 8080]

# --- 2. PRINT THE HEADER (Note: This is its own line now!) ---
print(f"--- Scanning Target: {target_ip} ---")

# --- 3. RUN THE LOOP ---
for port in ports_to_check:
    status = scan_port(target_ip, port)
    print(f"Port {port}: {status}")
