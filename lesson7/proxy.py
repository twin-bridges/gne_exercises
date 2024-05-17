import os
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("NETMIKO")
if not password:
    password = getpass("Enter your Netmiko password: ")

device = {
    "device_type": "cisco_xe",
    "host": "cisco1.bogus.com",
    "username": "jmorrow",
    "password": password,
    "ssh_config_file": "~/.ssh/ssh_config",
}

with ConnectHandler(**device) as nc:
    d = nc.send_command("show lldp neighbors detail")
    print(d)
