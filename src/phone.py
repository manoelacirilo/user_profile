class Phone:
    counter = 0

    def __init__(self, phone_number, phone_type):
        self.__id: int = Phone.counter + 1
        self.__phone_number = phone_number
        self.__phone_type = phone_type
        Phone.counter = self.__id

    def get_id(self):
        return self.__id

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number

    def get_phone_type(self):
        return self.__phone_type

    def set_phone_type(self, new_phone_type):
        self.__phone_type = new_phone_type

    def show_data(self):
        return f'Id: {self.get_id()}; Number: {self.get_phone_number()}; Type: {self.get_phone_type()}'

