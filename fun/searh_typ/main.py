"""
    Я Функция, и я ищу все файлы конкретного типа внутри папки.
    Я не трогаю папки внутри папки в которой ищу.
    Если я смогла найти что-то, я возвращаю внутри массива.
    Если я не смогла найти что-то я возвращаю None
    Если были проблемы я возвращаю булево-значения.
    Я дополнительная функция.
"""


def searh_typ(typ):
    Пробую получить список файлов:
        Список получен.
        список = clear(список, typ)# форматирование типа.

        Озвучить  конечный список файлов
    Иначе:
        Скажу что не смог прочитать папку.
    Финал:
        Пробую закрыть папку, или удалить изначальный массив.
        Этот блок сдесь не обьязателен, но должен быть хотябы пустым.

