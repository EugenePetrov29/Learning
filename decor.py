student_list = []
work = False
def add_a_Student(student):
    if student in student_list:
        print('Пользователь с таким именем уже существует')
    else:
        student_list.append(student)
        print("Привет " + student)
    return student_list
def delete_a_Student(student):
    if student in student_list:
        student_list.remove(student)
        print('Пользователь удален')
    else:
        print('Пользователь с таким именем не существует')
    return student_list
def exit():
    print("До свидания")
while not work:
    student = input("Введите своё имя: ")
    key = False
    while not key:
        print('''
        1.Add a Student
        2.Delete a Student (verification)
        3.Exit/Quit
        ''')
        answer = input("Введите номер: ")
        if answer == "1":
            add_a_Student(student)
        elif answer == "2":
            delete_a_Student(student)
        elif answer == "3":
            exit()
            key = True
    work = True