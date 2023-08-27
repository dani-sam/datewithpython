print('Welcome to love calculator')
name1 = input("what is ur name?")
name2 = input('what is their name?')
combined_string = name1+name2
lower_case_sting = combined_string.lower()
t = lower_case_sting.count('t')
r = lower_case_sting.count('r')
u = lower_case_sting.count('u')
e = lower_case_sting.count('e')
true = t + r + u + e

l = lower_case_sting.count('l')
o = lower_case_sting.count('o')
v = lower_case_sting.count('v')
e = lower_case_sting.count('e')
love = l + o + v + e

result = str(true) + str(love)
# print(type(result))
int_result = int(result)

if int_result <= 10 and int_result >= 90:
  print(f"your score is {result}%, you go together like coke and mentors")
elif int_result >= 40 and int_result <= 50:
  print(f"your score is {result}%, you are alright together")
else:
  print(f"your score is {result}")