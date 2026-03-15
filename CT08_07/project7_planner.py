while True:
    action = input('''What would you like to do?
a. Create a new task file
b. View all tasks
c. Add a new task
d. Delete a task
e. Mark a task as done
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
        f = open("CT08_07/tasks.txt", "a")
        task = input("Enter a new task: ")
        f.write(task + "\n")
        f.close()
        print("The task has been added successfully!")
    elif action == "d":
        f = open("CT08_07/tasks.txt", "r")
        lines = f.readlines()
        for line in range(len(lines)-1):
            print(f"{line+1}. {lines[line+1]}")
        while True:
            done = input("Which task number is completed? ").strip()
            if done.isnumeric():
                if int(done) < len(lines):
                    pass #continue work here

