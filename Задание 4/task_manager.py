from task import Task
from subtask import Subtask
from complex_task import ComplexTask


class TaskManager:
    
    id_series = 0
    
    def __init__(self):
        self.tasks = dict()
        self.subtasks = dict()
        self.complex_tasks = dict()
    
    
    def __get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1 
        return next_id_value
        
    def create_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_task = Task(current_id, name, description)
        self.tasks[current_id] = new_task
        return new_task
    
    def create_subtask(self, parent_id, name, description):
        current_id = self.__get_and_increment_id()
        new_task = Subtask(current_id, parent_id, name, description)
        self.subtasks[current_id] = new_task
        self.complex_tasks[parent_id].add_subtask(new_task)
        return new_task

    def create_complex_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_task = ComplexTask(current_id, name, description)
        self.complex_tasks[current_id] = new_task
        return new_task

    def get_tasks(self):
        return self.tasks
    
    def get_subtasks(self):
        return self.subtasks
    
    def get_complex_tasks(self):
        return self.complex_tasks
    
    def get_task_by_id(self, id):
        if id in self.tasks:
            return self.tasks[id]
        else:
            return None
    
    def get_subtask_by_id(self, id):
        if id in self.subtasks:
            return self.subtasks[id]
        else:
            return None
    
    def get_complex_task_by_id(self, id):
        if id in self.complex_tasks:
            return self.complex_tasks[id]
        else:
            return None
    
    def remove_task_by_id(self, id):
        if id in self.tasks:
            del self.tasks[id]
    
    def remove_subtask_by_id(self, id):
        if id in self.subtasks:
            parent_id = self.subtasks[id].get_parent_id()
            del self.subtasks[id]
            self.complex_tasks[parent_id].delete_subtask(id)

    def remove_complex_task_by_id(self, id):
        if id in self.complex_tasks:
            for subtask in self.complex_tasks[id].get_subtasks():
                subtask_id = subtask.get_id()
                del self.subtasks[subtask_id]
            del self.complex_tasks[id]
    
    def remove_task(self):
        pass
    
    def remove_subtask(self):
        pass
    
    def remove_complex_task(self):
        pass
    
    def update_status(self, id, status):
        if id in self.tasks:
            self.tasks[id].change_done_status(status)
        elif id in self.subtasks:
            self.subtasks[id].change_done_status(status)
