class Address:
    counter = 0

    def __init__(self, street, number, complement, city, state, cep):
        self.__id: int = Address.counter + 1
        self.__street = street
        self.__number = number
        self.__complement = complement
        self.__city = city
        self.__state = state
        self.__cep = cep
        Address.counter = self.__id

    def get_id(self):
        return self.__id

    def get_street(self):
        return self.__street

    def set_street(self, new_street):
        self.__street = new_street

    def get_number(self):
        return self.__number

    def set_number(self, new_number):
        self.__number = new_number

    def get_complement(self):
        return self.__complement

    def set_complement(self, new_complement):
        self.__complement = new_complement

    def get_city(self):
        return self.__city

    def set_city(self, new_city):
        self.__city = new_city

    def get_state(self):
        return self.__state

    def set_state(self, new_state):
        self.__state = new_state

    def get_cep(self):
        return self.__cep

    def set_cep(self, new_cep):
        self.__cep = new_cep

    def show_data(self):
        return f'Id: {self.get_id()}; {self.get_street()}, {self.get_number()}, {self.get_complement()}, ' \
               f'{self.get_city()} - {self.get_state()}, {self.get_cep()}'
