class Tasklist:
    def __init__(self):
        self._list = []

    def get_tasks(self):
        return 'no tasks' if not self._list else self._list
    
    def add_task(self, task):
        self._list.append(task)

    def complete_task(self, task):
        if task not in self._list:
            raise Exception('task not in list')
        return self._list.remove(task)
        