# Example code for lesson7
import os
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("NETMIKO")
if not password:
    password = getpass("Enter your Netmiko password: ")

# cisco1.bogus.com does not resolve, so use it as fictional domain
device = {
    "device_type": "cisco_xe",
    "host": "cisco1.bogus.com",
    "username": "jmorrow",
    "password": password,
}

start_time = datetime.now()
with ConnectHandler(**device) as nc:
    data = nc.send_command("show run")
    print(data)

# print(data)
end_time = datetime.now()
print(f"{end_time - start_time}")
