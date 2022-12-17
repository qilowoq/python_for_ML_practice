from task import Task

class Subtask(Task):
    # have complex task id : parent_id
    def __init__(self, id, parent_id, name, description):
        super().__init__(id, name, description)
        self.__parent_id = parent_id

    def get_parent_id(self):
        return self.__parent_id
    