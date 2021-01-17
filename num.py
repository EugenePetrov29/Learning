s = '\u2B1B'
o = " "

zero1 = s + s + s + o
zero2 = s + o + o + s + o
zero3 = s + o + o + s + o
zero4 = s + o + o + s + o
zero5 = s + s + s + o

one1 = s + s + o + o + o
one2 = o + o + s + o + o + o
one3 = o + o + s + o + o + o
one4 = o + o + s + o + o + o
one5 = s + s + s + o

two1 = s + s + s + o
two2 = o + o + o + o + s + o
two3 = s + s + s + o
two4 = s + o + o + o + o + o
two5 = s + s + s + o

three1 = s + s + s + o
three2 = o + o + o + o + s + o
three3 = s + s + s + o
three4 = o + o + o + o + s + o
three5 = s + s + s + o

four1 = s + o + o + s + o
four2 = s + o + o + s + o
four3 = s + s + s + o
four4 = o + o + o + o + s + o
four5 = o + o + o + o + s + o

five1 = s + s + s + o
five2 = s + o + o + o + o + o
five3 = s + s + s + o
five4 = o + o + o + o + s + o
five5 = s + s + s + o

six1 = s + s + s + o
six2 = s + o + o + o + o + o
six3 = s + s + s + o
six4 = s + o + o + s + o
six5 = s + s + s + o

seven1 = s + s + s + o
seven2 = o + o + o + o + s + o
seven3 = o + o + o + o + s + o
seven4 = o + o + o + o + s + o
seven5 = o + o + o + o + s + o

eith1 = s + s + s + o
eith2 = s + o + o + s + o
eith3 = s + s + s + o
eith4 = s + o + o + s + o
eith5 = s + s + s + o

nine1 = s + s + s + o
nine2 = s + o + o + s + o
nine3 = s + s + s + o
nine4 = o + o + o + o + s + o
nine5 = s + s + s + o

sep1 = o + o + o + o + o
sep2 = o + o + o + o + o
sep3 = o + o + o + o + o 
sep4 = o + s + o + o
sep5 = o + o + o + o + o

sep6 = o + o + o + o + o
sep7 = o + s + o + o
sep8 = o + o + o + o + o
sep9 = o + o + o + o + o
sep10 = o + o + o + o + o

zero = (zero1, zero2, zero3, zero4, zero5)
one = (one1, one2, one3, one4, one5)
two = (two1, two2, two3, two4, two5)
three = (three1, three2, three3, three4, three5)
four = (four1, four2, four3, four4, four5)
five = (five1, five2, five3, five4, five5)
six = (six1, six2, six3, six4, six5)
seven = (seven1, seven2, seven3, seven4, seven5)
eith = (eith1, eith2, eith3, eith4, eith5)
nine = (nine1, nine2, nine3, nine4, nine5)
sep = (sep1, sep2, sep3, sep4, sep5)


str1 = {'0' : zero1, '1' : one1, '2' : two1, '3' : three1, '4' : four1, '5' : five1, '6' : six1, '7' : seven1, '8' : eith1, '9' : nine1, ':' : [sep1, sep6]}

str2 = {'0' : zero2, '1' : one2, '2' : two2, '3' : three2, '4' : four2, '5' : five2, '6' : six2, '7' : seven2, '8' : eith2, '9' : nine2, ':' : (sep2, sep7)}

str3 = {'0' : zero3, '1' : one3, '2' : two3, '3' : three3, '4' : four3, '5' : five3, '6' : six3, '7' : seven3, '8' : eith3, '9' : nine3, ':' : (sep3, sep8)}

str4 = {'0' : zero4, '1' : one4, '2' : two4, '3' : three4, '4' : four4, '5' : five4, '6' : six4, '7' : seven4, '8' : eith4, '9' : nine4, ':' : (sep4, sep9)}

str5 = {'0' : zero5, '1' : one5, '2' : two5, '3' : three5, '4' : four5, '5' : five5, '6' : six5, '7' : seven5, '8' : eith5, '9' : nine5, ':' : (sep5, sep10)}
