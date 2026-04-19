
try:
    f = open("CT08_08/sherlock.txt", "r")
    text = f.read()
    # print(text) <-- task 1
    charcount = len(text)
    print(charcount) # <-- task 2
    vowels = {
        "a" : 0,
        "e" : 0,
        "i" : 0,
        "o" : 0,
        "u" : 0
    }
    for char in text:
        if char.lower() in vowels:
            vowels[char.lower()] += 1
    print(vowels) # <-- task 3

    vowelcount = 0
    for vowel in vowels:
        vowelcount += vowels[vowel]
    vowelpercent = round(vowelcount/charcount, 2)
    print(f"{vowelpercent}%")
    f = open("CT08_08/vowel_counts.txt", "w")
    try:
        f.write(f"Vowel count: {vowelcount}\nVowel percentage: {vowelpercent}%")
    except:
        print("There was an error in creating the new file.")
except FileNotFoundError:
    print("The file does not exist.")


f = open("CT08_08/sherlock.txt", "r")
words = f.read().lower().split()
newchar = []
for char in f.read():
    if char.isalnum() or char == " ":
        newchar.append(char.lower())
print("done")

word = input("What word are you searching for?: ").lower().strip()
newword = []
for char in word:
    if char.isalpha():
        newword.append(char)
word = "".join(newword)
wordcount = 0



while True:
    if word in words:
        wordcount += 1
        words.remove(word)
    else:
        break
print(f'The word "{word}" appears {wordcount} times.')