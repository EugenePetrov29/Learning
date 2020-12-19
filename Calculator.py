height = int(input("Введите свой рост, см = "))
waight = int(input("Введите свой вес, кг = "))
height /= 100
BMI = waight/(height**2)
print("Ваш индекс массы тела =", int(BMI))
if int(BMI)>=15 and int(BMI)<=40:
    s1= "15"
    list1 = list("="*26)
    num = int(BMI)-int(s1)
    list1[num]="|"
    s2 = ''.join(list1)
    s3 = "40"
    Grafic = s1 + s2 + s3
    print(Grafic)
    if int(BMI)>=15 and int(BMI)<=18:
        print('Недостаточный вес!')
    elif int(BMI)>18 and int(BMI)<=25:
        print('Нормальный вес!')
    elif int(BMI)>25 and int(BMI)<=30:
        print('Избыточная масса!')
    elif int(BMI)>30 and int(BMI)<=35:
        print('Ожирение! (I-степень)')
    elif int(BMI)>35 and int(BMI)<=40:
        print('Тяжелое ожирение! (II-степень)')
elif int(BMI)<15:
    print('Сильный недостаток веса!')
elif int(BMI)>40:
    print('Крайне тяжелое ожирение! (III - степень)')