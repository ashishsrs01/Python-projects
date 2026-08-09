def todo():

   
    def show_menu():
        print('\n-- Todo Menu --')
        print('Press 1 to view tasks')
        print('Press 2 to add task ')
        print('Press 3 to delete task ')
        print('Press 4 to Exit')

    def view_task():
         with open('Todo app/task.txt', 'r') as f:
             task = f.readlines()
             for task in task:
                print(task.strip())

    def add_task():
        print('\nEnter the task to add: ')
        t = input()
        with open('Todo app/task.txt', 'a') as f:
            f.writelines(t + '\n')
        print('\nTask added successfully!')

    def delete_task():
        print('\nEnter the task for deletion: ')
        t = input()
        with open('Todo app/task.txt', 'r') as f:
            task = f.readlines()

            if t in task:
                f.remove(t)
                print('\nTask deleted successfully!')
            else:
                print('\nTask not existed')


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
            print('\nentered value not accepted')

todo()


            

