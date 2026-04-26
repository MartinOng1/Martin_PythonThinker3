# Qns: Student Results File Processing

# You are given a text file called results.txt.
# Each line contains a student's name and mark, separated by a space.

# Example:
# Alex 92
# Ben 43
# Clara 78

# Your task:

# 1. Read the data from results.txt.

# 2. Convert the data into a dictionary called student_results.
#    The name should be the key.
#    The mark should be the value.

f = open('CT08_12/results.txt', 'r')
student_results = {}
for line in f.readlines():
    student_results[line.split()[0]] = int(line.split()[1])

# 3. With the dictionary, create another dictionary that count the student in the follow range:
# 0 - 50, 51 - 70, 71 - 90, 91 - 100

scores = {"0-50" : [],
          "51-70" : [],
          "71-90" : [],
          "91-100" : []}
for student in student_results:
    if student_results[student] <= 50:
        scores["0-50"].append(student)
    elif student_results[student] <= 70:
        scores["51-70"].append(student)
    elif student_results[student] <= 90:
        scores["71-90"].append(student)
    else:
        scores["91-100"].append(student)

# 4. Do a analysis of the score to get the following and print it to a output txt file 
# Min score: 
# Max Score:
# No of people in each range
# 0 - 50:  people
# 51 - 70: people
# 71 - 90: people
# 91 - 100: people
# the mode for range: __________
# average score:

scorer = {}
score = []
for student in student_results:
    scorer[student_results[student]] = student
    score.append(student_results[student])

with open('CT08_12/output.txt', 'w') as f:
    f.write(f'Lowest score: {min(score)} ({scorer[min(score)]})\n')
    f.write(f'Highest score: {max(score)} ({scorer[max(score)]})\n')
    score_range = {}
    for i in scores:
        f.write(f'Number of scorers who scored between {i}: {len(scores[i])}\n')
        score_range[len(scores[i])] = i
    f.write(f'Mode for range: {max(score_range)} ({score_range[max(score_range)]})\n')
    total = 0
    for i in score:
        total += i
    f.write(f'Average score: {total/len(score)}')