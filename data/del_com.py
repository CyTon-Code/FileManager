def del_comment(text, sep="\n", comment="/"):
	a = ""
	text += sep
	j = ""
	com = True
	not_skobki = True
	
	for i in text:
		if i == "'" and j != "\\":
			not_skobki = not not_skobki
		if i == comment and not_skobki:
			com = False
		
		if i == sep:
			com = True
		
		if com:
			a += i
		j = i
	return a
r = """

copy_paste: False;  // Эффективная технология для запуска приложений.
//c input
moving: True;  // Эффективно запускать библиотеки. без input.

args: False;  // Можно ли запускать команды в поле аргументов.
ants: False;  // Можно ли при старте запускать скрипты указанные в
//path_list_ants.
console: True;

path_list_py: {'', '/sys/', '/def/'};
path_list_ants: {'lib.ant', '/ants/index.ant', '/sys/system.ant'};

name: 'Queen';
home: '~';

title: '{name} {home}';
hello: '[{title}]$ ';  // Это приветсвенное сообщение перед вводом
//команды

check_open: True;  // Можно узнать существует ли?
check_read: True;  // Можно ли прочитать существующий?
check_edit: True;  // Можно ли редактировать существующий?
check_delete: False;  // Исполнитель не хотел бы удалять чужое.
check_create: False;  // Исполнитель не хотел бы создавать чужое.




"""
print(del_comment(r))
