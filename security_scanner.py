import requests

def get_location(ip):
    # We use http (not https) for this specific free API to avoid SSL errors
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    
    # This checks if the API actually found the IP
    if data.get("status") == "success":
        return f"{data['city']}, {data['country']}"
    else:
        # If it fails, this will tell us WHY (e.g., 'reserved range' or 'invalid query')
        return f"Error: {data.get('message', 'Unknown Error')}"

# Use a definitely public IP for the test
test_ip = "1.1.1.1"

print(f"--- Global Trace Initiated ---")
location = get_location(test_ip)
print(f"Target IP: {test_ip}")
print(f"Result: {location}")
print(f"--- Trace Complete ---")
