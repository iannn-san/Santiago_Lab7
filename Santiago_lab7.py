name = str(input("Enter your Name:"))
sect = str(input("Enter your section:"))

#prelim inputer hehe
prelims = float(input("Enter Preliminary Grade: "))
while prelims < 40 or prelims > 100:
    print("Error: Grade must be between 40 and 100.")
    prelims = float(input("Enter Preliminary Grade: "))

#midterm inputer
midterms = float(input("Enter Midterm Period Grade: "))
while midterms < 40 or midterms > 100:
    print("Error: Grade must be between 40 and 100.")
    midterms = float(input("Enter Midterm Grade: "))

#finals inputer
finals = float(input("Enter Final Grade: "))
while finals < 40 or finals > 100:
    print("Error: Grade must be between 40 to 100.")
    finals = float(input("Enter Final Grade: "))

final_percentage = (prelims * 0.3333) + (midterms * 0.3333) + (finals * 0.3333)

if 99 <= final_percentage <= 100:
    grade_point = 1.00
    description = "Excellent"
elif 96 <= final_percentage <= 98:
    grade_point = 1.25
    description = "Very Good"
elif 93 <= final_percentage <= 95:
    grade_point = 1.50
    description = "Good"
elif 90 <= final_percentage <= 92:
    grade_point = 1.75
    description = "Above Average"
elif 87 <= final_percentage <= 89:
    grade_point = 2.00
    description = "Satisfactory"
elif 84 <= final_percentage <= 86:
    grade_point = 2.25
    description = "Fair"
elif 81 <= final_percentage <= 83:
    grade_point = 2.50
    description = "Passed"
elif 78 <= final_percentage <= 80:
    grade_point = 2.75
    description = "Passed"
elif 75 <= final_percentage <= 77:
    grade_point = 3.00
    description = "Passed"
else:
    grade_point = 5.00
    description = "Failed"

print(f"\nFinal Percentage: {final_percentage:.2f}%")
print(f"Grade Point: {grade_point:.2f}")
print(f"Description: {description}")