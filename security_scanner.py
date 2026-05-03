
import requests

def get_detailed_intel(ip):
    # We are asking the API for the ISP and the 'Proxy/Hosting' flags
    url = f"http://ip-api.com/json/{ip}?fields=status,country,city,isp,proxy,hosting"
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("status") == "success":
            # Logic: If it's a proxy or hosting, it's 'Suspect'
            is_bot = "SUSPECT" if data.get("proxy") or data.get("hosting") else "CLEAN"
            return {
                "city": data.get("city"),
                "isp": data.get("isp"),
                "status": is_bot
            }
        return {"city": "Unknown", "isp": "Unknown", "status": "PRIVATE"}
    except:
        return {"city": "Error", "isp": "Error", "status": "ERROR"}

# --- THE WATCHLIST ---
suspects = ["8.8.8.8", "1.1.1.1", "104.21.19.201", "172.253.120.102"]

print(f"{'IP ADDRESS':<15} | {'STATUS':<10} | {'ISP':<20} | {'LOCATION'}")
print("-" * 70)

for ip in suspects:
    intel = get_detailed_intel(ip)
    print(f"{ip:<15} | {intel['status']:<10} | {intel['isp']:<20} | {intel['city']}")
