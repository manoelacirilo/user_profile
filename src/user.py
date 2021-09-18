
class User:
    counter = 0

    def __init__(self, name, birthdate, email, password, address, phones):
        self.__id: int = User.counter + 1
        self.__name = name
        self.__birthdate = birthdate
        self.__email = email
        self.__passoword = password
        self.__address = address
        self.__phones = phones
        User.counter = self.__id

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name) -> None:
        self.__name = new_name

    def get_birthdate(self):
        return self.__birthdate

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_password(self):
        return self.__passoword

    def set_password(self, new_password):
        self.__passoword = new_password

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        self.__address = new_address

    def get_phones(self):
        return self.__phones

    def add_phone(self, new_phone):
        self.__phones.append(new_phone)



