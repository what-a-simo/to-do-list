import json


FILENAME = 'tasks.json'


def load_tasks():
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print('Your to-do list is currently empty.')
        return False

    print('These are your tasks:')
    for i, (key, value) in enumerate(tasks.items(), 1):
        print(f'{i}. {value} {key}')
    return True


def complete_task(task, tasks):
    if task in tasks:
        tasks[task] = '[X]'
        print(f'Task "{task}" marked as completed!')
    else:
        print(f'Task "{task}" not found.')


def main():
    print('\nHi! This is a to-do list application.')

    tasks = load_tasks()

    while True:
        print('\n' + '=' * 27 + ' What do you want to do? ' + '=' * 27)
        print('1.   Add a task')
        print('2.   Remove a task')
        print('3.   View your tasks')
        print('4.   Complete a task')
        print('5.   Exit\n')

        choice = input('Your choice: ').strip()

        match choice:
            case '1':
                print('\n' + '=' * 27 + ' Add a task ' + '=' * 27)
                task = input('Write here your task: ').strip()
                if task:
                    tasks.update({task: '[ ]'})
                    save_tasks(tasks)
                    print('Task added successfully!')
                else:
                    print('Task cannot be empty.')

            case '2':
                print('\n' + '=' * 27 + ' Remove a task ' + '=' * 27)
                if show_tasks(tasks):
                    task = input('Remove task (type exact name): ').strip()
                    if task in tasks:
                        tasks.pop(task)
                        save_tasks(tasks)
                        print(f'Task "{task}" removed successfully.')
                    else:
                        print(f'Task "{task}" not found.')

            case '3':
                print('\n' + '=' * 27 + ' View your tasks ' + '=' * 27)
                show_tasks(tasks)

            case '4':
                print('\n' + '=' * 27 + ' Complete a task ' + '=' * 27)
                if show_tasks(tasks):
                    task = input('Choose which task do you want to complete: ')
                    complete_task(task, tasks)
                    save_tasks(tasks)

            case '5':
                print('\n' + '=' * 27 + ' Exit ' + '=' * 27)
                end = input('Are you sure? (y/n) ').strip().lower()
                if end == 'y':
                    break
                elif end != 'n':
                    print('Invalid input.')

            case _:
                print('\nInvalid choice. Please enter a number between 1 and 5.')

    print('\nThanks for using my application!')


if __name__ == '__main__':
    main()