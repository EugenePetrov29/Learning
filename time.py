
import os
import time
import datetime
import num


value = True
while True:
    ct = datetime.datetime.now()
    str_ct = ct.strftime('%H:%M:%S')
    time.sleep(1)
    for x in num.str1.keys():
        os.system('cls' if os.name == 'nt' else 'clear')
        if x == ':':
            if value == True:
                str_ct = str_ct.replace(x, str(num.str1[x][0]))
            else:
                str_ct = str_ct.replace(x, str(num.str1[x][1]))
            value = not value
        else:
            str_ct = str_ct.replace(x, str(num.str1[x]))
    print(str_ct)
    str_ct = ct.strftime('%H:%M:%S')
    for x in num.str2.keys():
        if x == ':':
            if value == True:
                str_ct = str_ct.replace(x, str(num.str2[x][0]))
            else:
                str_ct = str_ct.replace(x, str(num.str2[x][1]))
            value = not value
        else:
            str_ct = str_ct.replace(x, str(num.str2[x]))
    print(str_ct)
    str_ct = ct.strftime('%H:%M:%S')
    for x in num.str3.keys():
        if x == ':':
            if value == True:
                str_ct = str_ct.replace(x, str(num.str3[x][0]))
            else:
                str_ct = str_ct.replace(x, str(num.str3[x][1]))
            value = not value
        else:
            str_ct = str_ct.replace(x, str(num.str3[x]))
    print(str_ct)
    str_ct = ct.strftime('%H:%M:%S')
    for x in num.str4.keys():
        if x == ':':
            if value == True:
                str_ct = str_ct.replace(x, str(num.str4[x][0]))
            else:
                str_ct = str_ct.replace(x, str(num.str4[x][1]))
            value = not value
        else:
            str_ct = str_ct.replace(x, str(num.str4[x]))
    print(str_ct)
    str_ct = ct.strftime('%H:%M:%S')
    for x in num.str5.keys():
        if x == ':':
            if value == True:
                str_ct = str_ct.replace(x, str(num.str5[x][0]))
            else:
                str_ct = str_ct.replace(x, str(num.str5[x][1]))
            value = not value
        else:
            str_ct = str_ct.replace(x, str(num.str5[x]))
    print(str_ct)