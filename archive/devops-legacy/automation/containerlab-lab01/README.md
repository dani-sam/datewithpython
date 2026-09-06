# containerlab-lab01

3-router FRR lab using Containerlab + Docker.
Automated with Netmiko over SSH.

## Topology
R1 -- R2 -- R3

## Stack
- Containerlab + FRRouting (Alpine)
- Netmiko for SSH automation
- Python 3

## Files
- `lab01.yml` — Containerlab topology definition
- `first_connect.py` — connects to each router via SSH, prints hostname
- `healthcheck.py` — pings all nodes after deploy, reports reachability
- `NOTES.md` — engineering journal (what broke, what I learned)

## Setup

```bash
python3 -m venv netauto-env
source netauto-env/bin/activate
pip install -r requirements.txt
```

## Run

```bash
# Deploy lab
sudo containerlab deploy -t lab01.yml

# Check current IPs (they may change between deployments)
sudo containerlab inspect -t lab01.yml

# Clear stale SSH host keys if redeploying
ssh-keygen -R <each_node_IP>

# Activate venv
source ~/netauto-env/bin/activate

# Run connection script
python3 first_connect.py

# Run health check
python3 healthcheck.py
```

## Cleanup

```bash
sudo containerlab destroy -t lab01.yml
```

## Known Issue / Debugging Notes

The `frrouting/frr:latest` image is Alpine-based, not
Debian/Ubuntu. If modifying the exec block:
- Use `apk`, not `apt-get`
- Include `ssh-keygen -A` to generate missing SSH host keys
- Install the `shadow` package for reliable `chpasswd`
- Wrap `chpasswd` in `sh -c "..."` for correct pipe handling
  in Containerlab's exec context

IPs are dynamically assigned and may change between
redeployments — always check with `containerlab inspect`
before running the Python scripts.
