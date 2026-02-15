# Predefined data
answer_key = ["A", "B", "B", "D"]  # Correct answers for the quiz
student_answers = {
    "john": ["A", "C", "B", "D"],
    "jane": ["A", "B", "B", "D"],
    "alice": ["A", "C", "C", "D"],
    "bob": ["A", "B", "B", "D"]
}

#repeat asking user for command until they exit. grade students first so that scores can be used for remaining functions
#grade: find number of correct answers for each student
#avg: add all scores and divide by num of students
#highest: set highest score, and loop though to see if there are any students with same or higher score.
#display: loop through scores and print each name with their score
#menu: print all options, ask user to choose a command. Do not allow user to type other things.

def grade_all_students(ans, anskey):
    quiz_scores = {}
    for student in ans:
        correct = 0
        counter = 0
        for a in ans[student]:
            if a == anskey[counter]:
                correct += 1
            counter += 1
        quiz_scores[student] = correct
    return quiz_scores

def calculate_average_score(scores):
    total = 0
    for score in scores:
        total += scores[score]
    return total / len(scores)

def find_highest_scorer(scores):
    max = -99999
    maxlist = []
    for score in scores:
        if scores[score] > max:
            max = scores[score]
            maxlist = [score]
        elif scores[score] == max:
            maxlist.append(score)
    return maxlist

def display_results(scores):
    for score in scores:
        print(f"{score.title()}: {scores[score]}")

def menu_system(grades):
    while True:
        command = input("Enter a command:\n1. Calculate average score\n2. Find highest scorer\n3. Display all results\n4. Exit program\nYour command: ")
        if command == "1":
            print(f"The average score is {calculate_average_score(grades)}")
        elif command == "2":
            print("The highest scorers are:")
            for scorer in find_highest_scorer(grades):
                print(scorer)
        elif command == "3":
            display_results(grades)
        elif command == "4":
            print("Exiting Program...")
            break
        else:
            print('Please type "1", "2", "3", or "4" only.')

menu_system(grade_all_students(student_answers, answer_key))