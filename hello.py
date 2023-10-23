# create a list to store  the values as  tasks
tasks = []

# define a function to add a task
def addtask(i):
    tasks.append(i)

# define a function to view all tasks
def viewtasks():
    for i in tasks:
        print(i)

# define a function to remove a task
def deletetask(i):
    tasks.remove(i)


def main():
    while True:
        print("\nA list of things to do")
        print("-----------")
        print("1. Add  a Task")
        print("2. View  all theTasks")
        print("3. Delete a particular Task")
        print("4. Quit")

        option = input("enter your choice: ")

        if option == "1":
            task = input("Enter task: ")
            addtask(task)
        elif option == "2":
            viewtasks()
        elif option == "3":
            task = input("Enter task to delete: ")
            deletetask(task)
                       
        elif option == "4":
            break
        else:
            print("Invalid option, please try again.")

# run the main function
if __name__ == "__main__":
    main()