import whois

def lookup_domain(domain_name):
    print(f"--- Investigating: {domain_name} ---")
    try:
        # This reaches out to the global WHOIS database
        details = whois.whois(domain_name)
        
        print(f"Registrar: {details.registrar}")
        print(f"Creation Date: {details.creation_date}")
        print(f"Country: {details.country}")
        print(f"Emails: {details.emails}")
        
    except Exception as e:
        print(f"Investigation failed: {e}")

# Let's test it on a major target
target = "mesrs.dz"
try:
    details = whois.whois(target)
    # This prints the RAW text sent back from the server
    print("--- RAW DATA FROM ALGERIA ---")
    print(details.text) 
except Exception as e:
    print(f"The automated tool struggled: {e}")
lookup_domain(target)
