def todo():

    tasks = []

    def show_menu():
        print('-- Todo Menu --')
        print('Press 1 to view tasks')
        print('Press 2 to add task ')
        print('Press 3 to delete task ')
        print('Press 4 to Exit')

    def view_task():

        if not tasks:
            print('NO task exist yet!')
        else:
            print(tasks)

    def add_task():
        print('Enter the task to add: ')
        task = input()
        tasks.append(task)
        print('Task added successfully!')

    def delete_task():
        print('Enter the task for deletion: ')
        task = input()
        if task in tasks:
            tasks.remove(task)
            print('Taks deleted successfully')
        else:
            print('this task not existed')
        

    while True:

        show_menu()

        try:
            n = int(input())
        except ValueError:
            print('Entered value not accepted')

        if n == 1:
            view_task()
        elif n ==2: 
            add_task()
        elif n == 3:
            delete_task()
        elif n == 4:
            break
        else:
            print('entered value not accepted')

todo()


            

