def usr(arg):
    l = [".q", ".quit", ".e", ".exit", ".c", ".close"]
    if arg in l:
        exit()


def main(args):
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
