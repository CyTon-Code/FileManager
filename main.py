# Я узнаю где можно подключать модули а где нет

# функция модуль(args):
    # Я узнаю каким способом подключать модуль
    # Я подключаю указаным способом модуль и передаю ему args.

# Если можно запускать используя argv:
    # Я запускаю функцию модуль и передаю ей массив argv как args кроме
    #argv[0].

# Если можно запускать скрипты:
    # Я читаю скрипты и по строчно превращая в массив за правилами
    #APD-1, запускаю функцию модуль и передаю ей каждый раз новый
    #массив args.

# Я запускаю консольный режим, если можно:
    # Я требую ввести строку: команда и аргументы.
    # Если в строке есть не парное количество НЕЭКРАНИРОВАННЫХ кавычек: или
    #если нарушены APD-1:
        # Запускаю дописание к строке \n> .
    # Превращая строку в массив за правилами APD-1, я запускаю функцию модуль
    #и отдаю ей свой массив как args.

"""
    argv - аргументы полученные при запуске ANT.
    args - аргументы терминала ANT.
    APD-1 - документация как должни писатся команды и аргументы в ANT.
"""

