# Day 2: The Automated Evidence Scanner 

file_path = "server_logs.txt"

print(f"---Scanning Evidence File:{file_path }---")

with open(file_path,"r") as evidence:
  for line in evidence:
   #.strip()to clean up extra spaces 
    clean_line = line.strip()

    if"CRITICAL" in clean_line or "ALERT" in clean_line:
                                                    print(f"[!]THREAT DETECTED:{clean_line}")
  print("---Investifation Complete---")                                              
