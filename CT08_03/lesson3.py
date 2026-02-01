students = {
    "Alice" : 85,
    "Bob" : 90,
    "Charlie" : 78
}

students["John"] = 56
students["Elias"] = 99
students["Kok Seng"] = 65

print(f"Student Grades: {students}")

grade = input("Which student do you want to look for? ")
if grade in students:
    print(students[grade])
else:
    print("That student is not in our database.")