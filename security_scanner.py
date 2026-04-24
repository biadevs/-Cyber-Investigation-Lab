import requests

def get_location(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("status") == "success":
            return f"{data['city']}, {data['country']}"
        else:
            return "Private/Internal IP"
    except:
        return "Connection Error"

# --- THE INVESTIGATION BOARD ---
# A list of suspicious IPs found in our "logs"
suspects = [
    "8.8.8.8",         # Google
    "1.1.1.1",         # Cloudflare
    "192.168.1.50",    # Private (Local)
    "104.21.19.201",   #unknown Web Server 
    "172.253.120.102"  # Unknown Web Server
]

print(f"{'IP ADDRESS':<15} | {'LOCATION':<25}")
print("-" * 45)

for ip in suspects:
    location = get_location(ip)
    print(f"{ip:<15} | {location:<25}")
