def todo():

    TASK_FILE = 'task.txt'

    def show_menu():
        print('\n-- Todo Menu --')
        print('Press 1 to view tasks')
        print('Press 2 to add task ')
        print('Press 3 to delete task ')
        print('Press 4 to Exit')

    def view_task():
        try:
            with open(TASK_FILE, 'r') as f:
                lines = f.readlines()
                if not lines:
                    print('\nNo tasks found.')
                    return
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print('\nTask file not found. No tasks to show.')
        except Exception as e:
            print(f'\nError reading tasks: {e}')

    def add_task():
        try:
            print('\nEnter the task to add: ')
            t = input().strip()
            if not t:
                print('\nEmpty task not added.')
                return
            with open(TASK_FILE, 'a') as f:
                f.writelines(t + '\n')
            print('\nTask added successfully!')
        except Exception as e:
            print(f'\nError adding task: {e}')

    def delete_task():
        try:
            print('\nEnter the task for deletion: ')
            t = input().strip()
            if not t:
                print('\nNo task entered.')
                return
            try:
                with open(TASK_FILE, 'r') as f:
                    lines = f.readlines()
            except FileNotFoundError:
                print('\nTask file not found. Nothing to delete.')
                return

            stripped = [ln.rstrip('\n') for ln in lines]
            if t in stripped:
                # keep tasks that are not the one to delete
                remaining = [s + '\n' for s in stripped if s != t]
                with open(TASK_FILE, 'w') as f:
                    f.writelines(remaining)
                print('\nTask deleted successfully!')
            else:
                print('\nTask does not exist')
        except Exception as e:
            print(f'\nError deleting task: {e}')


    while True:

        show_menu()

        try:
            n = int(input())
        except ValueError:
            print('Entered value not accepted')
            continue
        except KeyboardInterrupt:
            print('\nExiting.')
            break

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


            

