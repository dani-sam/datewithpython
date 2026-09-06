## 2025-06-17

### What I did
Built health_check.py — pings all lab nodes after deploy using containerlab inspect JSON output

### What broke
- json.load() vs json.loads() — stdout is a string not a file object
- Variable inside quotes in subprocess list — treated as literal string not code

### What I learned
- subprocess returncode 0 = success, non-zero = failure
- containerlab inspect --format json structure: lab_data['lab01'] is the node list

### What to automate next
- Run health_check.py automatically after every containerlab deploy
