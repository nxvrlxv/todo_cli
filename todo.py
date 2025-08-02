class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.done = False
        self.description = description
        self.priority = priority

    def __str__(self):
        return (f"task name: {self.title}\n "
              f"task description: {self.description}\n"
              f" task priority: {self.priority}\n "
              f"task status: {self.done}")

    def mark_done(self):
        self.done = True



class TaskManager:
    def __init__(self):
        self.tasks = []

    def __str__(self):
        if not self.tasks:
            return "Нет никаких задач."

        tasks = ''
        for i, task in enumerate(self.tasks, 1):
            tasks += f"Задача {i}:\n{task}\n"

        return f"Вот все ваши задачи:\n {tasks}"

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_index):
        if not self.tasks:
            return "Нечего удалять, задач нет :3"
        if task_index < 1 or task_index > len(self.tasks):
            raise IndexError("Недопустимый индекс! Выберите другой).")

        self.tasks.pop(task_index-1)
        print(f"Успешно удалена задача {task_index}!")

running = True
manager = TaskManager()

while running:
    print(f"Добро пожаловать в меню, выберите действие:\n"
          f"1. Добавить задачу\n"
          f"2. Показать все задачи\n"
          f"3. Отметить задачу выполненной\n"
          f"4. Удалить задачу\n"
          f"5. Выйти из приложения")
    number = input()
    if number == '1':
        title = input('Введите заголовок задачи')
        description = input('Введите описание задачи')
        priority = input('Введите приоритет задачи')
        task = Task(title, description, priority)
        manager.add_task(task)
        input('Нажмите Enter чтобы выйти в меню...')
        continue
    if number == '2':
        print(manager.tasks)
        input('Нажмите Enter чтобы выйти в меню...')
        continue
    if number == '3':
        if not manager.tasks:
            print('Нет ни одной добавленной задачи, добавьте, чтобы изменить ее статус.')
            input('Нажмите Enter чтобы выйти в меню...')
            continue
        else:
            print('Выберите задачу (номер):')
            print(manager.tasks)
            number_of_task = int(input())
            manager.tasks[number_of_task-1].mark_done()
            input('Нажмите Enter чтобы выйти в меню...')
            continue
    if number == '4':
        print('Выберите задачу (номер), которую хотите удалить:')
        print(manager.tasks)
        number_of_task = int(input())
        manager.delete_task(number_of_task)
        input('Нажмите Enter чтобы выйти в меню...')
        continue
    if number == '5':
        running = False


#taskk = Task("Прогулка на велике", "Прогулка на велике вдоль набережной", "Средний")
#task1 = Task("Занятия спортом", "Поход в тренажерный зал", "Высокий")




#manager.add_task(taskk)
#manager.add_task(task1)

#print(manager)
#manager.delete_task(100)
#print(manager.tasks)
