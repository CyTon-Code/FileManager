from   as check_file

def not_really_or_really(link, path, result=True):
    if check_file(link) or not check_file(path):  # if a or !b is true:
        return result
    return not result  # иначе: reverse


def not_really_and_really(link, path, result=True):
    if check_file(link) and not check_file(path):  # if a or !b is true:
        return result
    return not result  # иначе: reverse


def moves(link, path):
    # если ссылки равны:
        # скажу что переместил.  # это не обязательно.
    
    если "первая ссылка указывает не на файл" или (
            "вторая ссылка указывает на файл"):
        скажу "переместить файл не могу!"
    
    переместить файл(с link к path)
    
    если "первая ссылка указывает не на файл" или (
            "вторая ссылка указывает на файл"):
        скажу "переместить файл удалось!"
    иначе:
        скажу "эта операция не сработала корректно!"
    # если "link указывает не на файл" или "path указывает на файл":
    #     скажу "Я не могу переместить."
    #скажу = (ссылка на файл которого недолжно быть, ссылка на файл
    #который есть, значение которое нужно вернуть если ссылки коректны)
    
    if not_really_or_really(link, path):  # Если переместить нереально:
        return None
    # скажу "Я могу переместить файл.":
    
    os.replace(link, path)  # Перемещаю файл.
    
    # после перемещения: a должен исчезнуть, а b должен появится.
    
    if not_really_and_really(link, path):
        pass
    
    если "link указывает не на файл" или "path указывает на файл":
        скажу "Я смогла переместить файл."
    иначе:
        скажу "Я не смогла переместить файл."
    return скажу

