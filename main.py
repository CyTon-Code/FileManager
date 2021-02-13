# import  as to_list
# import  as path
# import  as ant_typ
# import  as system

home = __file__

hi_sms = "$ "


def mode_manual():  # Manual command input mode:
    no_exit = True
    command = None
    
    while no_exit:
        command = to_list(input(hi_sms))
        type_ant = ant_typ(command)
        
        if type_ant == "usr":  # .exit .help ...
            system(command[0])
        elif type_ant == "sys":
            pass  # import: home/sys   return bool or Exeption
        else:  # module:
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
