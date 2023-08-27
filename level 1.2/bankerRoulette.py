import random
names_string = input("Give me everybody's names , separated by a comma. ")

names = names_string.split(", ")
# Get the total number of items of list.
num_items = len(names)
# Generate random number 0 and last index
random_pay = random.randint(0,num_items - 1)
# Optional we use choice method
# pay_name = random.choice(names)
pay_name = names[random_pay]
print(f"{pay_name} is going to buy the meal today!")