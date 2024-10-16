class TasksModel:
    def __init__(self):
        self.tasks = [{'name': 'поспать', 'status': 'в ожидании'}]

    def get_tasks(self):
        return self.tasks

    def add_task(self, name):
        task = {'name': name, 'status': 'в ожидании'}
        self.tasks.append(task)

    def complete_task(self, task_number):
        self.tasks[task_number]['status'] = 'выполнено'

    def delete_task(self, task_number):
        if task_number < len(self.tasks):
            self.tasks.pop(task_number)
        else:
            print('\nТакой задачи нет')


class View:

    @staticmethod
    def show_all_tasks(tasks):
        for number, task in enumerate(tasks, 1):
            print(f"\n{number}. {task['name']} - {task['status']}")

    @staticmethod
    def show_add_task():
        return input('\nВведи название задачи: ')

    @staticmethod
    def show_complete_task():
        return int(input('\nВведи номер задачи: '))

    @staticmethod
    def show_delete_task():
        return int(input('\nВведи номер задачи: '))


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self):
        tasks = self.model.get_tasks()

        self.view.show_all_tasks(tasks)
        task_name = self.view.show_add_task()
        self.model.add_task(task_name)

        self.view.show_all_tasks(tasks)

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_all_tasks(tasks)

    def complete_task(self):
        task_number = self.view.show_complete_task()
        task_number -= 1
        self.model.complete_task(task_number)

    def delete_task(self):
        task_number = self.view.show_delete_task()
        task_number -= 1
        self.model.delete_task(task_number)


model = TasksModel()
view = View()
contr = Controller(model, view)

while True:
    print("\n1 - Добавить задачу")
    print("2 - Выполнить задачу")
    print("3 - Посмотреть список задач")
    print("4 - Удалить задачу")
    print("5 - Выйти")

    choice = input(f'\nЧто ты хочешь сделать? ')

    if choice == '1':
        contr.add_task()
    elif choice == '2':
        contr.complete_task()
    elif choice == '3':
        print('\nВот ваши задачи')
        contr.show_tasks()
    elif choice == '4':
        contr.delete_task()
    elif choice == '5':
        print("\nДо свидания!")
        break
