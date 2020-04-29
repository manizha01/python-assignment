

num_of_courses = int(input("How many courses did you finish?  "))
#print(num_of_courses)

counter = 1
course_mark = []
while int(counter) <= num_of_courses:
    course_mark.append(float(input(f"Enter your mark for Course {counter}:  ")))
    counter +=1

    # I use this for loop to print list (array) item in new lines
for elem in course_mark:
    print(elem)
#print(course_mark)
    #print(counter)

total = 0
for number in course_mark:
    total = total + number
    #print(total)

    average = total/num_of_courses
result = input(f"Your average for your {num_of_courses} courses is:  {average}")
#print("your average for your courses is:" + str(avg))

if average >= 90  and average <= 100:
    print("your grade is A+")
elif average >= 80 and average <=89:
    print("your grade is B")
elif average >= 70 and average <=79:
    print("your grade is C")
elif average >= 60 and average <= 69:
    print("your grade is D")
elif avg < 60:
    print("your grade is F")
