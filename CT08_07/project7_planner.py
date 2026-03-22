while True:
    action = input('''What would you like to do?
a. Create a new task file
b. View all tasks
c. Add a new task
d. Mark a task as done
e. Delete a task
f. Exit the program
Your choice: ''').strip().lower()
    if action not in ["a", "b", "c", "d", "e", "f"]:
        print('Please only type letters "a" through "f".')
    elif action == "a":
        try:
            f = open("CT08_07/tasks.txt", "r")
        except FileNotFoundError:
            f = open("CT08_07/tasks.txt", "w")
            f.write("My Task List\n")
            f.close()
            print("File created successfully!")
        else:
            while True:
                overwrite = input("The file already exists. Would you like to overwrite it? (Y/N): ").strip().lower()
                if overwrite == "y":
                    f = open("CT08_07/tasks.txt", "w")
                    f.write("My Task List\n")
                    f.close()
                    print("File overwritten successfully!")
                    break
                elif overwrite == "n":
                    print("The file was not overwritten.")
                    break
                else:
                    print('Please type "Y" or "N" only.')
    elif action == "b":
        f = open("CT08_07/tasks.txt", "r")
        lines = f.readlines()
        if len(lines) == 1:
            print("No tasks found!")
        else:
            for line in range(len(lines)-1):
                print(f"{line+1}. {lines[line+1]}")
    elif action == "c":
        task = input("Enter a new task: ")
        f = open("CT08_07/tasks.txt", "r")
        tasks = f.readlines()
        if task + "\n" in tasks:
            print("That task already exists.")
        else:
            f = open("CT08_07/tasks.txt", "a")
            f.write(task + "\n")
            f.close()
            print("The task has been added successfully!")
    elif action == "d":
        f = open("CT08_07/tasks.txt", "r")
        lines = f.readlines()
        for line in range(len(lines)-1):
            print(f"{line+1}. {lines[line+1]}")
        while True:
            breaked = False
            done = input("Which task number is completed? ").strip()
            if done.isnumeric():
                if int(done) >= len(lines) or int(done) < 1:
                    print("Please enter a valid task number")
                else:
                    if lines[int(done)][len(lines[int(done)])-7:] == "(Done)\n":
                        while True:
                            choice = input("That task is already marked as done. Would you like to\na. Mark undone\nb. Cancel\nYour Choice: ").strip().lower()
                            if choice not in ["a", "b"]:
                                print('Please type "a" or "b" only.')
                            elif choice == "a":
                                lines[int(done)] = lines[int(done)][:len(lines[int(done)])-8] + "\n"
                                breaked = True
                                break
                            else:
                                breaked = True
                                break
                    else:        
                        lines[int(done)] = lines[int(done)][:len(lines[int(done)])-1] + " (Done)\n"
                        break
            else:
                print("Please enter a number.")
            if breaked:
                break
        
        with open("CT08_07/tasks.txt", "w") as f:
            f.writelines(lines)
    elif action == "e":
        f = open("CT08_07/tasks.txt", "r")
        lines = f.readlines()
        for line in range(len(lines)-1):
            print(f"{line+1}. {lines[line+1]}")
        while True:
            done = input("Which task number would you like to delete? ").strip()
            if done.isnumeric():
                if int(done) >= len(lines) or int(done) < 1:
                    print("Please enter a valid task number")
                else:
                    lines.pop(int(done))
                    break
            else:
                print("Please enter a number.")
        
        with open("CT08_07/tasks.txt", "w") as f:
            f.writelines(lines)
    elif action == "f":
        print("Exiting program...")
        break
                

#there is a possibility for the following output:
# a. Create a new task file
# b. View all tasks
# c. Add a new task
# d. Mark a task as done
# e. Delete a task
# f. Exit the program
# Your choice: b
# 1. write essay

# 2. study exam (Done (Done)write essay
# try to fix this issue
#1. prevent duplicate task
#2. prevent duplicate done
#3. allow done to be undone if needed.

