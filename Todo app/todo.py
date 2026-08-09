def todo():

    tasks = []

    def show_menu():
        print('-- Todo Menu --')
        print('Press 1 to view tasks')
        print('Press 2 to add task ')
        print('Press 3 to delete task ')
        print('Press 4 to Exit')

    def view_task():

        if tasks is []:
            print('NO task exist')
        else:
            print(tasks)

    def add_task():
        print('Enter the task to add: ')
        task = input()
        tasks.append(task)

    def delete_task():
        print('Enter the task for deletion: ')
        task = input()
        tasks.remove(task)

    while True:

        show_menu()

        try:
            n = int(input())
        except ValueError:
            print('Entered value not accepted')

            

