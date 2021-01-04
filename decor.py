student_list = []
work = False
def add_a_Student(student):
        student_list.append(student)
        print("Привет " + student)

def decorator(func):
    def wraper_decorator(*args):
        if args[0] not in student_list:
            return print('Пользователя с таким именем не существует')
        value = func(*args)
        return func
    return wraper_decorator

@decorator
def delete_a_Student(student):
    student_list.remove(student)
    print('Пользователь удален')

def exit():
    print("До свидания")
while not work:
    name = input("Введите своё имя: ")
    key = False
    while not key:
        print('''
        1.Add a Student
        2.Delete a Student (verification)
        3.Exit/Quit
        ''')
        answer = input("Введите номер: ")
        if answer == "1":
            add_a_Student(name)
        elif answer == "2":
            delete_a_Student(name)
        elif answer == "3":
            exit()
            key = True
    work = True