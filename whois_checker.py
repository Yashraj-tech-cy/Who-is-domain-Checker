# WHOIS Domain Info Checker
# For educational purposes only

import whois
import csv

# Step 1: Ask user to enter a domain
domain_name = input("Enter a domain name (like google.com): ")

try:
    # Step 2: Get domain info using whois library
    info = whois.whois(domain_name)

    # Step 3: Show information on the screen
    print("\n--- Domain Information ---")
    print("Domain Name:", info.domain_name)
    print("Registrar:", info.registrar)
    print("Creation Date:", info.creation_date)
    print("Expiration Date:", info.expiration_date)
    print("Name Servers:", info.name_servers)

    # Step 4: Save info to a text file
    with open("domain_info.txt", "w") as file:
        file.write(f"Domain Name: {info.domain_name}\n")
        file.write(f"Registrar: {info.registrar}\n")
        file.write(f"Creation Date: {info.creation_date}\n")
        file.write(f"Expiration Date: {info.expiration_date}\n")
        file.write(f"Name Servers: {info.name_servers}\n")

    # Step 5: Save info to a CSV file
    with open("domain_info.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Domain Name", "Registrar", "Creation Date", "Expiration Date", "Name Servers"])
        writer.writerow([info.domain_name, info.registrar, info.creation_date, info.expiration_date, info.name_servers])

    print("\n Info saved to 'domain_info.txt' and 'domain_info.csv' successfully.")

except Exception as e:
    print("\n Could not fetch domain info. Reason:", e)
