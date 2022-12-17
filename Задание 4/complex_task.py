from task import Task

class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self, id, name, description):
        super().__init__(id, name, description)
        self.subtasks = dict() 

    def add_subtask(self, subtask):
        self.__done_status = False
        self.subtasks[id] = subtask

    def delete_subtask(self, id):
        del self.subtasks[id]

    def get_subtasks(self):
        return self.subtasks

    def get_done_status(self):
        for id in self.subtasks:
            if not self.subtasks[id].get_done_status():
                return False
        self.__done_status = True
        return True