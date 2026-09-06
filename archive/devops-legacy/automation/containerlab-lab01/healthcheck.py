import subprocess
import json

rs = subprocess.run(
    ["sudo", "clab", "inspect", "-t", "lab01.yml", "-f", "json"],
    capture_output= True,
    text = True
)


# print("Return Code:", rs.returncode)
# print("STDOUT:")
# print(rs.stdout)
# print("STDERR:")
# print(rs.stderr)

# print(type(lab_data))
# print(lab_data)
# print(lab_data.keys())

if rs.returncode == 0:
    lab_data = json.loads(rs.stdout)

    for node in lab_data['lab01']:
        # print(
        #     f"Node: {node['name']} | "
        #     f"Status: {node['status']} | "
        #     f"IP Address: {node['ipv4_address'].split('/')[0]}"
        # )
        ip = node['ipv4_address'].split('/')[0]
        ping_rs = subprocess.run(["ping", "-c", "2", ip],
        capture_output = True, text= True
        )

        print(f"\nNode: {node['name']}")

        if ping_rs.returncode == 0:
            print("Reachable")
        else:
            print("Unreachable")
        
    
else:
    print(f"Error running command: {rs.stderr}")




