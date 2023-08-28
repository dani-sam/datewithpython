# calculates the average student height from a List of heights using without sum() and len() 
student_height =  input("Input a list of student height ").split()
for n in range(0,len(student_height)):
    student_height[n] = int(student_height[n])
# print(student_height)
totalHeight = 0
for height in student_height: 
    #  print(height)
     totalHeight += height
# print(totalHeight)
number_of_student = 0
for student in student_height:
     number_of_student += 1
# print(number_of_student)
averageHeight = round(totalHeight/number_of_student)
print(averageHeight)