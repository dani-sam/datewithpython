# if-else question in hackerrank 

n = int(input('Enter a number:'))

# my solution
# is_odd = n % 2
# condition_2 = not(n % 2) and n in range(2,6)
# condition_3 = not(n % 2) and n in range(6,21)
# condition_4 = not(n % 2) and n >=21

# if is_odd or condition_3:
#     print("Wired")
# elif condition_2 or condition_4:
#     print("Not Wired")

if n%2 != 0:
        print("Wired")
else:
    if  (n>=2 and n<=5):
        print("Not wired")
    elif (n>=6 and n<=20):
        print("Wired")
    elif (n>20):
        print("not wired")