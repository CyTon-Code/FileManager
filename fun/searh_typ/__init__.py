"""
Я функция читаю масив и тип файла():  # Удаление чужих типов.
    удаляю адресса файлов чужих тип.
    Повторяю пока ИЗМЕНЯЮ СВОЕ МНЕНИЕ:
        Я НЕ ИЗМЕНИЛ СВОЕ МНЕНИЕ.
        Читаю по строчно массив:
            Если элемент не заканчивает на нужный тип:
                удаляю элемент
                Я ИЗМЕНИЛ СВОЕ МНЕНИЕ.
    верну масив
"""

def end_typ(link, typ):  # Нужного ли типа файл?  - встроенный модуль
    n = len(typ)  # -n -это нулевой єлемен массива.

    if n > len(link) or typ in ("", "."):
        return None  # тип файла содержит больше букв, чем имя файла или
        #указанный тип есть в чорном списке.

    i = 1  # последний элемент масив это: n-1 или -1

    while i <= n:  # Читаю строку типа и сравниваю с строкой.
        if link[-i] != typ[-i]:  # Если нашел не схожие буквы в типе:
            return False

        i += 1

    return True


def clear_typ(array, typ):  # Доп модуль.
    flag = True

    while flag:
        flag = False

        i = 0
        n = len(array)

        while i < n:
            if not end_typ(array[i], typ):

                array.remove(array[i])  # del i

                n = len(array)  # Update n
                flag = True  # Скажу что я менял

            i += 1

    return array


el = ["1.txt", "i.del", "o.txt", "text.txt", "de"]
print(clear_typ(el, ".txt"))
print(end_typ("e.l", ".l"))
