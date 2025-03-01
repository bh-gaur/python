import ipaddress

def is_private_ip(ip):
    return ipaddress.ip_address(ip).is_private

# Example Usage
ip_address = input("Enter ip: ")
if is_private_ip(ip_address):
    print(f"{ip_address} is a Private IP")
else:
    print(f"{ip_address} is a Public IP")
