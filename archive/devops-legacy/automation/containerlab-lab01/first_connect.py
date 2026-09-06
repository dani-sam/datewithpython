from netmiko import ConnectHandler

devices = [
    {"name": "R1", "host": "172.20.20.4"},
    {"name": "R2", "host": "172.20.20.2"},
    {"name": "R3", "host": "172.20.20.3"},
]

for device in devices:
    conn = ConnectHandler(
        device_type="linux",
        host=device["host"],
        username="root",
        password="admin",
    )
    output = conn.send_command("hostname")
    print(f"{device['name']} → {output.strip()}")
    conn.disconnect()
