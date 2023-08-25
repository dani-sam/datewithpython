# factorial Generator
# Calculate the Factorial of a Number
# Using recursion method
        

def fact(n):
    return 1 if (n==1 or n==0) else n * fact(n - 1);

num=6;
print(fact(num))
             


