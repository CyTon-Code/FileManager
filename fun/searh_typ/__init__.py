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

from internal.correct_type import end_typ


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
