try:
    f = open("CT08_09/encrypted_note.txt", "r")
    newchar = []
    for char in f.read():
        if char.isalnum() or char == " ":
            newchar.append(char.lower())
    cleaned = "".join(newchar)
    words = cleaned.split()
    decrypted = []
    for word in words:
        decrypted.append(word[0])
    hidden_message = "".join(decrypted)
    print(hidden_message)

    with open("CT08_09/hidden_message.txt", "w") as f:
        f.write(hidden_message[::-1])
                     
except FileNotFoundError:
    print("ERROR: The encrypted note has vanished. Is someone trying to hide the truth?")