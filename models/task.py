class Task:
    def __init__(self, task_id, task_title, task_description, task_completed=False):
        self.task_id = task_id
        self.task_title = task_title
        self.task_description = task_description
        self.task_completed = task_completed

    def to_dict(self):
        return {
            'id': self.task_id,
            'title': self.task_title,
            'description': self.task_description,
            'completed': self.task_completed
        }
    
    def update_task(self, task_title, task_description, completed=False):
        self.task_title = task_title
        self.task_description = task_description
        self.task_completed = completed
    
    