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



task = Task("Купить хлеб", "Зайти в магазин и купить хлеб", "средний")
print(task)  # тут статус должен быть False
task.mark_done()
print(task)  # а тут уже True
