# import  as to_list
# import  as path

hi_sms = "$ "


def mode_manual():  # Manual command input mode:
    no_exit = True
    command = None
    
    while no_exit:
        command = to_list(input(hi_sms))
        if command[0] == ".exit":
            no_exit = False
    pass


def mode_include(link: str):  # Executing commands from a file:
    pass


def mode_args():  # Executing commands using arguments at startup:
    pass


mode_arguments()

for link in path:
    mode_include(link)

mode_manual()
