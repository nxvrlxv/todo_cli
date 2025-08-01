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



task = Task("Прогулка на велике", "Прогулка на велике вдоль набережной", "Средний")
task1 = Task("Занятия спортом", "Поход в тренажерный зал", "Высокий")


manager = TaskManager()

manager.add_task(task)
manager.add_task(task1)

print(manager)