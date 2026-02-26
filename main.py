import json


FILENAME = 'tasks.json'

def load_tasks():
    try:
        with (open(FILENAME, 'r') as file):
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
        print(f'{i}. {key} {value}')
    return True

def main():
    print('\nHi! This is a to-do list application.')

    tasks = load_tasks()

    while True:
        print('\n=========================== What do you want to do? ===========================')
        print('1.   Add a task')
        print('2.   Remove a task')
        print('3.   View your tasks')
        print('4.   Exit\n')

        choice = input('Your choice: ').strip()

        match choice:
            case '1':
                print('\n=========================== Add a task ===========================')
                task = input('Write here your task: ').strip()
                if task:
                    tasks.update({task: '[ ]'})
                    save_tasks(tasks)
                    print('Task added successfully!')
                else:
                    print('Task cannot be empty.')

            case '2':
                print('\n=========================== Remove a task ===========================')
                if show_tasks(tasks):
                    task = input('Remove task: ')
                    removed = tasks.pop(task)
                    save_tasks(tasks)
                    print(f'Task "{removed}" removed successfully.')

            case '3':
                print('\n=========================== View your tasks ===========================')
                show_tasks(tasks)

            case '4':
                print('\n=========================== Exit ===========================')
                end = input('Are tou sure? (y/n) ').strip().lower()
                if end == 'y':
                    break
                elif end != 'n':
                    print('Invalid input')

            case _:
                print('\nInvalid choice. Please enter a number between 1 and 4.')

    print('\nThanks for using my application!')

if __name__ == '__main__':
    main()