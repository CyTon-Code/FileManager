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

from internal.equal_type import equal_type


def clear_typ(array: list, typ: str) -> list:  # Доп модуль.
    flag = True  # Я менял внутри списка.

    while flag:
        flag = False  # Я не менял внутри списка.

        i = 0
        n = len(array)

        while i < n:
            if not equal_type(array[i], typ):
                array.remove(array[i])  # del i

                n = len(array)  # Update n
                flag = True  # Я менял внутри списка.

            i += 1

    return array


"""  test:
el = ["1.txt", "i.del", "o.txt", "text.txt", "de"]
print(clear_typ(el, ".txt"))
print(equal_type("e.l", ".l"))
"""
