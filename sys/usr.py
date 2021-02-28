def usr(key, value):
	if key in [".q", ".quit", ".c", ".close", ".e", ".exit"]:  # Выйти:
		exit()
	elif key in [".i", ".info"]:  # Узнать подробнее об args команды:
		pass
	elif key in [".h", ".help"]:  # Получить список args команды:
		pass
	elif key in [".d", ".doc"]:  # Полная документация об команде:
		pass
	elif key in [".v", ".version"]:  # Узнать версию команды.
		pass
	else:
		print("key:", key, "not difened!")
