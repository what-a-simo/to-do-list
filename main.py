def main():
    print('\nHi! This is a to-do list application.')

    tasks = []

    while True:
        print('\n=========================== What do you want to do? ===========================')
        print('1.   Add a task')
        print('2.   Remove a task')
        print('3.   View your tasks')
        print('4.   Exit\n')

        choice = input('Your choice: ')
        print(choice)

        match choice:
            case '1':
                print('\n=========================== Add a task ===========================')
                task = input('Write here your task: ')
                tasks.append(task)
                continue
            case '2':
                print('\n=========================== Remove a task ===========================')
                print('These are your tasks:')
                for i, task in enumerate(tasks, 1):
                    print(f'{i}. {task}')
                idx = int(input('Remove task (idx): '))
                if 1 <= idx <= len(tasks):
                    tasks.pop(idx - 1)
                continue
            case '3':
                print('\n=========================== View your tasks ===========================')
                print('These are your tasks:')
                for i, task in enumerate(tasks, 1):
                    print(f'{i}. {task}')
                continue
            case '4':
                print('\n=========================== Exit ===========================')
                end = input('Are tou sure? (y/n) ')
                if end == 'y':
                    break
                elif end == 'n':
                    continue
                else:
                    print('Invalid input')
                    continue

    print('\nThanks for using my application!')

if __name__ == '__main__':
    main()