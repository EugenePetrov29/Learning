#Задание №1
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
i = a and b and c and "Нет нулевых значений!!!"
print(i)
#Задание №2
d = a or b or c or "Введены все нули!"
print(d)
#Задание №3/4
if a > (b+c):
    print(a-b-c)
elif a < (b+c):
    print(b+c-a)
#Задание №5/6
if a > 50 and (a<b or a<c):
    print("Вася")
elif a > 5 or (b==7 and c==7):
    print("Петя")
else:
    print("Значения не соответсвуют никакому имени!")