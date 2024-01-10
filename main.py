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

    def make_boss(self, boss):
        self.__boss = boss

    def make_worker(self, worker):
        self.__workers.append(worker)

    def __str__(self):
        boss_str = f"Директор: {self.boss}" if self.boss else "Директор не назначен"
        workers_str = "\n".join(str(worker) for worker in self.workers)
        return f"Фирма: {self.name_of_work}\n{boss_str}\nСотрудники:\n{workers_str}"

    def create_work():
        name_of_work = input("Введите название фирмы: ")
        return Work(name_of_work)

    def create_boss():
        while True:
            name = input("Введите имя директора: ")
            if name.isalpha():
                break
            else:
                print("Ошибка: Имя должно состоять только из букв. Попробуйте снова.")

        surname = input("Введите фамилию директора: ")

        while True:
            age = input("Введите возраст директора: ")
            try:
                age = int(age)
                break  # Если возраст успешно преобразован в целое число, завершаем цикл
            except ValueError:
                print("Ошибка: Возраст должен быть числом. Попробуйте снова.")

        return Boss(name, surname, age)

    def create_worker():
        while True:
            name = input("Введите имя сотрудника: ")
            if name.isalpha():
                break
            else:
                print("Ошибка: Имя должно состоять только из букв. Попробуйте снова.")

        surname = input("Введите фамилию сотрудника: ")

        while True:
            age = input("Введите возраст сотрудника: ")
            try:
                age = int(age)
                break  # Если возраст успешно преобразован в целое число, завершаем цикл
            except ValueError:
                print("Ошибка: Возраст должен быть числом. Попробуйте снова.")

        return Worker(name, surname, age)

    def menu():
        work = None
        boss = None

        while True:
            print("Главное меню:")
            print("1. Создать фирму.")
            print("2. Создать директора(количество - 1).")
            print("3. Создать сотрудника.(количество - не ограничено)")
            print("4. Вывести информацию о сотруднике.")
            print("5. Вывести информацию о директоре.")
            print("6. Вывести информацию о фирме.")
            print("7. Выход из программы ")

            choose = input("Выберите пункт меню: ")

            if choose == "1":
                work = create_work()
                print("Фирма создана.")
                input("Нажмите Enter, чтобы продолжить...")
            elif choose == "2":
                if work:
                    boss = create_boss()
                    work.make_boss(boss)
                    print("Директор назначен.")
                else:
                    print("Сначала создайте фирму.")
                input("Нажмите Enter, чтобы продолжить...")
            elif choose == "3":
                if work:
                    worsker = create_worker()
                    work.make_worker(worker)
                    print("Сотрудник создан.")
                else:
                    print("Сначала создайте фирму.")
                input("Нажмите Enter, чтобы продолжить...")
            elif choose == "4":
                if work and work.workers:
                    for i, worker in enumerate(work.workers, start=1):
                        print(f"{i}. {worker}")
                else:
                    print("Нет сотрудников.")
                input("Нажмите Enter, чтобы продолжить...")
            elif choose == "5":
                if boss:
                    print(boss)
                else:
                    print("Нет директора.")
                input("Нажмите Enter, чтобы продолжить...")
            elif choose == "6":
                if work:
                    print(work)
                else:
                    print("Фирма не создана.")
                input("Нажмите Enter, чтобы продолжить...")
            elif choose == "7":
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор. Пожалуйста, выберите снова.")
if __name__ == "__main__":
    menu()