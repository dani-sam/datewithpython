def patternmatch(line, pattern):
    l = len(line)
    p = len(pattern)
    
    for i in range (l-p+1):
        match = True
        for j in range (p):
            if line[i+j] != pattern[j]:
                match = False
                break
        if match:
            return i;
    return -1

line = "python is popular"
pattern = "tho"
r = patternmatch(line, pattern)
if r != 1:
    print(f"pattern found at postion", r)
else:
    print("pattern not found")