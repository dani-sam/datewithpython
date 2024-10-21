# Text based Calculator

def get_number(num):
    while True:
        operand = input("Number "+ str(num) +": ")
        try:
            return float(operand)
    
        except:
            print("invalid number, try again.")


operand1 = get_number(1)
operand2 = get_number(2)
sign = input("Sign: ")


result = 0
if sign == "+":
    result = operand1 + operand2
elif sign == "-":
    result = operand1 - operand2
elif sign == "*":
    result = operand1 * operand2
elif sign == "/":
    if operand2 != 0:
        result = operand1 / operand2
    else:
        print("Division by zero.")
else:
    print("Invalid sign!!!")
print(result)