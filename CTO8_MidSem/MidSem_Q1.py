"""
============================================================
Q1. Quiz Auto-Marker
============================================================
You are building an auto-marker system for a multiple-choice quiz.
The program must compare a student's answers with the answer key.
It should calculate the score, identify which questions were wrong, and assign a grade.

- Write 3 functions:
    1) score_quiz(key, ans)
    2) wrong_questions(key, ans)
    3) grade(score, total)
- Do not change the function names or parameters.
- After writing your functions, uncomment the test code at the bottom to test.

============================================================
"""

# ============================================================
# Step 1: Write function score_quiz(key, ans)
# ============================================================
# - key and ans are lists of equal length
# - Compare answers at the same position
# - Return total number of correct answers
# ============================================================

def score_quiz(key, ans):
    sum = 0
    for i in range(len(key)):
        if key[i] == ans[i]:
            sum += 1
    return sum

# ============================================================
# Step 2: Write function wrong_questions(key, ans)
# ============================================================
# - Return a list of question numbers (starting from 1) that are wrong
# - If all answers are correct, return an empty list
# ============================================================

def wrong_questions(key, ans):
    wrong = []
    for i in range(len(key)):
        if key[i] != ans[i]:
            wrong.append(i+1)
    return wrong

# ============================================================
# Step 3: Write function grade(score, total)
# ============================================================
# - Compute percentage = (score / total) * 100
# - Return:
#     "A" if percentage >= 80
#     "B" if percentage >= 70
#     "C" if percentage >= 60
#     "D" otherwise
# ============================================================

def grade(score, total):
    numgrade = score/total * 100
    if numgrade >= 80:
        return "A"
    elif numgrade >= 70:
        return "B"
    elif numgrade >= 60:
        return "C"
    else:
        return "D"

# ============================================================
# Step 4: Main Code Testing
# ============================================================
# Uncomment after writing your functions

def test(answer_key, student_ans):
    score = score_quiz(answer_key, student_ans)
    wrong = wrong_questions(answer_key, student_ans)
    final_grade = grade(score, len(answer_key))
    print("Score:", score)
    print("Wrong Questions:", wrong)
    print("Grade:", final_grade)

answer_key1 = ["B","D","A","A","C","B","C","D","B","A"]
student_ans1 = ["B","D","C","A","C","B","C","A","B","A"]
answer_key2 = ["A", "B", "C", "D"]
student_ans2 = ["A", "B", "C", "D"]
answer_key3 = ["A","B","B","A","A","C","C","A"]
student_ans3 = ["B","C","D","B","C","A","C","A"]
test(answer_key1, student_ans1)
test(answer_key2, student_ans2)
test(answer_key3, student_ans3)