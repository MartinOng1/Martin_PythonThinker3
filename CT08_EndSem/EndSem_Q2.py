"""
============================================================
Q2. Review Text Analysis
============================================================
You are given a text file containing customer reviews.
The program must analyse the reviews and generate a rating.

Program Requirements:
- Read the contents of the file "reviews.txt"
- Count the total number of characters in the file
- Count how many reviews contain "good"
- Count how many reviews contain "bad"
- Calculate the percentage of good reviews
- Determine the overall rating:
    70% and above → Positive
    40% to 69% → Mixed
    Below 40% → Negative
- Save the results into "review_results.txt" and also print the results to the console

Note:
- The counting must be case-insensitive
- The percentage must be rounded to 2 decimal places
- If there are no valid reviews, the percentage should be 0

Print and save the result in this format:
    Review Text Analysis
    ------------------------------
    Total Characters: <number>
    Good Reviews: <number>
    Bad Reviews: <number>
    Percentage of Good Reviews: <value>%
    Overall Rating: <rating>

============================================================
"""

# ============================================================
# Step 1: Read file contents
# ============================================================

with open("CT08_EndSem/reviews.txt", "r") as f:

# ============================================================
# Step 3: Count characters and good or bad reviews
# ============================================================
    totalchar = len(f.read())

with open("CT08_EndSem/reviews.txt", "r") as f:
    good = 0
    bad = 0
    for review in f.readlines():
        if "good" in review.lower():
            good +=1
        if "bad" in review.lower():
            bad +=1

# ============================================================
# Step 4: Calculate percentage and rating
# ============================================================

with open("CT08_EndSem/reviews.txt", "r") as f:
    lines = len(f.readlines())
    if good == 0 or lines == 0:
        percent = 0
    else:
        percent = round(good/lines*100, 2)

    if percent >= 70:
        rating = "Positive"
    elif percent >= 40:
        rating = "Mixed"
    else:
        rating = "Negative"

# ============================================================
# Step 5: Write results to file
# ============================================================

with open("CT08_EndSem/review_results.txt", "w") as f:
    f.writelines(f"""
Review Text Analysis
------------------------------
Total Characters: {totalchar}
Good Reviews: {good}
Bad Reviews: {bad}
Percentage of Good Reviews: {percent}%
Overall Rating: {rating}
""")

# ============================================================
# Step 6: Print results to console
# ============================================================

print((f"""
Review Text Analysis
------------------------------
Total Characters: {totalchar}
Good Reviews: {good}
Bad Reviews: {bad}
Percentage of Good Reviews: {percent}%
Overall Rating: {rating}
"""))