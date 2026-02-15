attendance_dict = {
    "Alice" : [True, True, False],
    "Bob" : [False, True, False],
    "Charlie" : [True, False, False]
}

def take_attendance(attendance):
    for student in attendance:
        while True:
            present = input(f"Is {student} present? ").strip()
            if present == "True":
                attendance[student].append(True)
                break
            elif present == "False":
                attendance[student].append(False)
                break
            else:
                print('Please type "True" or "False" only.')
    return attendance

def attendance_percentage(student, attendance):
    trueNum = 0
    for i in attendance[student]:
        if i:
            trueNum += 1
    return round(trueNum / len(attendance[student]) * 100, 2)

def notify_low_attendance(attendance, threshold):
    low_attendance = []
    for student in attendance:
        if attendance_percentage(student, attendance) < threshold:
            low_attendance.append(student)
    return low_attendance

def view_attendance(attendance):
    for student in attendance:
        print(f"{student}: {attendance[student]}")

while True:           
    choice = input('''- 1: Take Attendance​
- 2: Calculate Attendance Percentage for a Student​
- 3: Notify Low Attendance​
- 4: View Attendance
- 5: Exit Program​
Your choice: ''').strip()
    if choice not in ["1", "2", "3", "4", "5"]:
        print('Please type "1", "2", "3", "4", or "5" only.')
    else:
        if choice == "1":
            take_attendance(attendance_dict)
            print("Attendance updated!")
        elif choice == "2":
            while True:
                student = input("Who's attendance percentage would you like to check? ").strip()
                if student in attendance_dict:
                    break
                else:
                    print("That student is not in our database.")
            print(attendance_percentage(student, attendance_dict))
        elif choice == "3":
            while True:
                threshold = input("What is the percentage threshold? ").strip()
                if threshold.isnumeric():
                    threshold = int(threshold)
                    break
                else:
                    print("Please enter a numeric value.")
            print(notify_low_attendance(attendance_dict, threshold))
        elif choice == "4":
            view_attendance(attendance_dict)
        else:
            print("Exiting program...")
            break
