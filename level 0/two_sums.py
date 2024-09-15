# leetcode practice
# Double for loop.Brute force.O(n^2) 
n = [3,2,4]
target = 6
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if n[i] + n[j] == target:
          print([i,j])

    
