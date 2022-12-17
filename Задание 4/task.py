class Task:
    def __init__(self, id, name, description):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__done_status = False
        
    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_done_status(self):
        return self.__done_status

    def change_done_status(self, done_status):
        self.__done_status = done_status
