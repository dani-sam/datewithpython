height = input('Enter your height in m:')
weight = input('Enter your weight in kg:')

height_as_float = float(height)
weight__as_int = int(weight)

# Using the exponent operator **
bmi = weight__as_int / height_as_float ** 2

# or using multiplication & PEMDAS
# bmi = weight__as_int / (height_as_float * height_as_float)

print(bmi)