oper2 = 'x'
try:
    while oper2 == 'x':
        f_num = float(input('Введите число: '))
        oper = input('Введите операцию: ')
        s_num = float(input('Введите второе число: '))
        if oper == '+':
            print(f_num + s_num)
        elif oper == '-':
            print(f_num - s_num)
        elif oper == '*':
            print(f_num * s_num)
        elif oper == '/':
            print(f_num / s_num)
        else:
            if oper != '+-*/':
                print('Вы ввели некорректную операцию!')

        oper2 = input("Введите 'x', чтобы продолжить ")
except ValueError:
    print('Вы ввели некоректное значение !')
