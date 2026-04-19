def caesar_shift_character(char, key, mode):
    if mode == "encrypt":
        return chr(((ord(char)-32 + key)%95)+32)
    elif mode == "decrypt":
        return chr(((ord(char)-32 - key)%95)+32)

def caesar_shift_sentence(sentence, key, mode):
    final = []
    for char in sentence:
        final.append(caesar_shift_character(char, key, mode))
    return "".join(final)

def caesar_shift_list(sentences, key, mode):
    final = []
    for sentence in sentences:
        final.append(caesar_shift_sentence(sentence, key, mode))
    return final

def caesar_shift_file(input_filename, output_filename, key, mode):
    f = open(input_filename, "r")
    sentences = f.readlines()
    stripped = []
    for sentence in sentences:
        stripped.append(sentence.strip("\n"))
    output = caesar_shift_list(stripped, key, mode)
    f = open(output_filename, "w")
    for line in output:
        f.write(line + "\n")
    f.close()

#task 5
#caesar_shift_file("CT08_11/encrypted.txt", "CT08_11/decrypted.txt", 12, "decrypt")

def menu_system():
    while True:
        action = input("a. Character shift\nb. Sentence shift\nc. List shift\nd. File shift\ne. Exit program\nYour choice: ").strip().lower()
        if action not in ["a", "b", "c", "d", "e"]:
            print('Please only type "a", "b", "c", "d", or "e".')
        elif action == "a":
            while True:
                char = input("Enter a character to shift: ")
                if len(char) != 1:
                    print("Please enter one character only.")
                    continue
                key = input("Enter a key: ")
                if not key.isnumeric():
                    print("Please type a number.")
                    continue
                mode = input("a. Encrypt\nb. Decrypt\nYour choice: ").strip().lower()
                if mode != "a" and mode != "b":
                    print('Please type only "a" or "b".')
                    continue
                else:
                    if mode == "a":
                        mode = "encrypt"
                    else:
                        mode = "decrypt"
                    break
            print(caesar_shift_character(char, int(key), mode))
        elif action == "b":
            while True:
                sentence = input("Enter a sentence: ")
                key = input("Enter a key: ")
                if not key.isnumeric:
                    print("Please type a number.")
                    continue
                mode = input("a. Encrypt\nb. Decrypt\nYour choice: ").strip().lower()
                if mode != "a" and mode != "b":
                    print('Please type only "a" or "b".')
                    continue
                else:
                    if mode == "a":
                        mode = "encrypt"
                    else:
                        mode = "decrypt"
                    break
            print(caesar_shift_sentence(sentence, int(key), mode))
        elif action == "c":
            sentences = []
            while True:
                sentence = input("Enter a sentence (press enter to stop): ")
                if sentence == "":
                    break
                else:
                    sentences.append(sentence)
            while True:
                key = input("Enter a key: ")
                if not key.isnumeric:
                    print("Please type a number.")
                    continue
                mode = input("a. Encrypt\nb. Decrypt\nYour choice: ").strip().lower()
                if mode != "a" and mode != "b":
                    print('Please type only "a" or "b".')
                    continue
                else:
                    if mode == "a":
                        mode = "encrypt"
                    else:
                        mode = "decrypt"
                    break
            print(caesar_shift_list(sentences, int(key), mode))
        elif action == "d":
            while True:
                key = input("Enter a key: ")
                if not key.isnumeric:
                    print("Please type a number.")
                    continue
                mode = input("a. Encrypt\nb. Decrypt\nYour choice: ").strip().lower()
                if mode != "a" and mode != "b":
                    print('Please type only "a" or "b".')
                    continue
                else:
                    if mode == "a":
                        mode = "encrypt"
                    else:
                        mode = "decrypt"
                    break
            output_filename = input("What file would you like to cipher? ")
            while True:
                input_filename = input("What file would you like to cipher? ")
                try:
                    caesar_shift_file(input_filename, output_filename, int(key), mode)
                except FileNotFoundError:
                    print("That file does not exist.")
                else:
                    break
        elif action == "e":
            print("Exiting program...")
            break                

menu_system()