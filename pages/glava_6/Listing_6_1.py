# Листинг 6.1
def my_fun_1(x, y):  # Определяем функцию пользователя
    z = x + y / 2 + x ** 3 - y ** 2
    print("Это работает функция - my_fyn_1")
    print('z =', z)
    print('-'*40)
    return

def my_fun_2(par_1, par_2):  # Определяем функцию пользователя
    print("Это работает функция - my_fyn_2")
    z = par_1 + par_2
    print('z =', z)
    return

# Это точка входа в программу (начало)
print("   --- Начало работы модуля - Listing_6_1 ---")
a = 2
b = 3
my_fun_1(a, b)  # Вызов функции my_fun_1

arg_1 = 'Привет '
arg_2 = 'Python!'
my_fun_2(arg_1, arg_2)  # Вызов функции my_fun_2

print('  --- Конец работы модуля - Listing_6_1 ---')