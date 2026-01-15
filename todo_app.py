print("=== My To-Do App ===")
# Simple CLI To-Do App
# Created while learning Python

while True:
    # Menu
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Exit")
    i = input("enter the action : ")
    
    if i == "3":
        print("Goodbye!")
        break
        
    elif i == "1":
        with open("task.txt","a") as f:
            T = input("Enter the task : ")
            f.write(T + "\n")
        print("Task added successfully!")
        
    elif i == "2":
        try:
            with open("task.txt", "r") as f:
                view = f.read()
                print(view)
        except FileNotFoundError:
            print("No task yet!")
    else :
        print("you entered wrong action try again! ")
