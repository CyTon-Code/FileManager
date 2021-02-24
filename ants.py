def system(key, value=""):
    if key in (".q", ".quit", ".e", ".exit", ".c", ".close"):  # Выйти:
        exit()

    elif key in (".i", ".info"):  # Узнать подробнее об args команды:
        pass

    elif key in (".h", ".help"):  # Получить список args команды:
        pass

    elif key in (".d", ".doc"):  # Полная документация об команде:
        pass

    elif key in (".v", ".version"):  # Узнать версию команды.
        pass

    else:
        print("key: {key} not difened!".format(key))


def main(args):
    no_exit = True
    command = None

    while no_exit:
        command = to_list(input(hi_sms))
        type_ant = ant_typ(command)

        if type_ant == "usr":
            system(command[0])

        elif type_ant == "sys":
            pass  # import: home/sys   return bool or Exeption

        else:  # module:
            pass  # import: home/def
