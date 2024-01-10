class Worker:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f"{self.name} {self.surname}, Возраст: {self.age}"


class Boss:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f"{self.name} {self.surname}, Возраст: {self.age}"


class Work:
    def __init__(self, name_of_work):
        self.__name_of_work = name_of_work
        self.__boss = None
        self.__workers = []

    @property
    def name_of_work(self):
        return self.__name_of_work

    @property
    def boss(self):
        return self.__boss

    @property
    def workers(self):
        return self.__workers