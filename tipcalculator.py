print("Welcome to the tip calculator")
total_bill = input('what was the total bill amount? $')
total_bill_as_float = float(total_bill)
tip = float(input("what percentage tip would u like to give? 10,12 or 15:"))
s_people = int(input("how many people to split the bill? "))
tip_with_bill = tip / 100
per_bill = total_bill_as_float * tip_with_bill
spl_bill = (total_bill_as_float + per_bill) / s_people
each_people = round(spl_bill,2)
print(f"Each person should pay: $ {each_people}")

