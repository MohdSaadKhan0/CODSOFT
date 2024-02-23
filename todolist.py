class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed.')
        else:
            print(f'Task "{task}" not found.')

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("Press 1 to Add Task")
        print("Press 2 to Remove Task")
        print("Press 3 to Show Tasks")
        print("Press 4 to Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Exiting the to-do list program")
            break
        else:
            print("Invalid. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
