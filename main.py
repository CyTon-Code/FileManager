import mode

# args:
import sys

if len(sys.argv) > 1:
	mode.arg(sys.argv)

# ants:
path = open_bd("path_list")

if len(path) > 0 and type(path) == list:
	for link in path:
		mode.include(link)

# console:
no_exit = True

while no_exit:
	cmd = input()
	ant(cmd)


def ant(cmd: str):
	to_list(cmd)
	ant_list(cmd)
	pass


def include(link: str):
	with open(link, 'r') as f:
		line = f.read().splitlines():
	for cmd in line:
		ant(cmd)

def arg(args):
	i, n = 0, len(args)
	
	while i < n:
		if args[i] == "-arg" and type(args[i+1]) == list:
			ant_list(args[i + 1])
		i += 1
pass

# import  as to_list
# import  as path
# import  as ant_typ
# import sys.usr as system

home = __file__
bash = None
hi_sms = "$ "


def mode_manual():  # Manual command input mode:
    no_exit = True
    command = None
    
    while no_exit:
        command = to_list(input(hi_sms))
        type_ant = ant_typ(command)
        if type_ant == "var":  # $?
			if command[0] == "$?":
				print(bash)
        elif type_ant == "usr":  # .exit .help ...
            system(command[0],command[1])
        elif type_ant == "sys":
			bash = sys_use_module()
            pass  # import: home/sys   return bool or Exeption
        else:  # module:
			bash = use_module()
            pass  # import: home/def
    pass


def mode_include(link: str):  # Executing commands from a file:
    # Reading a file line by line.
    pass


def mode_args():  # Executing commands using arguments at startup:
    pass


mode_arguments()

for link in path:
    mode_include(link)

mode_manual()
