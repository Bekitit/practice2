name = input("Enter Your Name:  ")
mark = []

for i in range(1,6):
    score = float(input("Enter mark for subject: " + str(i) + "  "))
    mark.append(score)
average = sum(mark) / len(mark)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B' 
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F' 
print("Name: " + name)
print("Average: " + str(average))
print("Grade: " + grade)                    