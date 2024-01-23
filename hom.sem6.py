from typing import List

class User:
    def __init__(self, surname, firstname, patronymic):
        self.surname = surname
        self.firstname = firstname
        self.patronymic = patronymic

    def __str__(self):
        return f"{self.surname} {self.firstname} {self.patronymic}"

class Teacher(User):
    def __init__(self, teacher_id, surname, firstname, patronymic):
        super().__init__(surname, firstname, patronymic)
        self.teacher_id = teacher_id

    def get_teacher_id(self):
        return self.teacher_id

    def set_info(self, surname, firstname, patronymic):
        self.surname = surname
        self.firstname = firstname
        self.patronymic = patronymic

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, {super().__str__()}"

class TeacherService:
    def __init__(self, teacher_list: List[Teacher] = []):
        """
        Принцип открытости/закрытости:
        Конструктор класса TeacherService.

        Parameters:
            teacher_list (List[Teacher]): Список учителей, который может быть передан при создании объекта.
        """
        self.teacher_list = teacher_list
        # Определение максимального идентификатора учителя при создании сервиса.
        self.max_teacher_id = max([teacher.get_teacher_id() for teacher in self.teacher_list], default=0)

    def get_all(self):
        return self.teacher_list

    def create(self, surname, firstname, patronymic):
        teacher = Teacher(self.max_teacher_id + 1, surname, firstname, patronymic)
        self.max_teacher_id += 1
        self.teacher_list.append(teacher)

    def edit_teacher(self, teacher_id, surname, firstname, patronymic):
        """
        Принцип подстановки Барбары Лисков:
        Редактирование информации об учителе по его идентификатору.

        Parameters:
            teacher_id (int): Идентификатор учителя, которого нужно отредактировать.
            surname (str): Новая фамилия.
            firstname (str): Новое имя.
            patronymic (str): Новое отчество.
        """
        for teacher in self.teacher_list:
            if teacher.get_teacher_id() == teacher_id:
                teacher.set_info(surname, firstname, patronymic)

class TeacherView:
    def print_teachers(self, teacher_list: List[Teacher]):
        """
        Принцип инверсии зависимостей:
        Вывод информации о учителях в консоль.

        Parameters:
            teacher_list (List[Teacher]): Список учителей для вывода.
        """
        for teacher in teacher_list:
            print(teacher)

class TeacherController:
    def __init__(self, teacher_service, teacher_view):
        self.teacher_service = teacher_service
        self.teacher_view = teacher_view

    def create(self, surname, firstname, patronymic):
        self.teacher_service.create(surname, firstname, patronymic)

    def edit_teacher(self, teacher_id, surname, firstname, patronymic):
        self.teacher_service.edit_teacher(teacher_id, surname, firstname, patronymic)

    def print_teachers(self):
        teachers = self.teacher_service.get_all()
        self.teacher_view.print_teachers(teachers)

# Пример использования:

# Создание объектов сервиса и представления
teacher_service = TeacherService()
teacher_view = TeacherView()
teacher_controller = TeacherController(teacher_service, teacher_view)

# Инициализация списка учителей
teachers = [Teacher(1, "Ivanov", "Ivan", "Ivanovich"), Teacher(2, "Petrov", "Petr", "Petrovich")]
teacher_service = TeacherService(teachers)

# Вывод списка учителей
teacher_controller.print_teachers()

# Создание нового учителя
teacher_controller.create("Sidorov", "Sidor", "Sidorovich")
teacher_controller.create("Mirovaev", "Miron", "Mironovich")

# Вывод обновленного списка учителей
teacher_controller.print_teachers()
