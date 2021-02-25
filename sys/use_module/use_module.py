"""
    The module works only through import.
    Via os.system or Return (RUN) - doesn't work.
"""

from sys.moves_module.main import moves

# TODO import  as using
# TODO import  as check_open

if __name__ == "__main__":  # If not imported, I exit is the module:
    print("I am is Module!!! Bye Bye!!!")
    exit()  # Answer: I'm leaving, I'm a module.


def use_module(link: str) -> bool or Exception:  # I am trying to run a module:
    """
        This module is one of those who can connect other modules.
        This module treats each module as a person (by moving, not copying).
    """  # Credo: Connecting the selected module...
    path = ""
    if check_open(path) and not check_open(link):
        moves(link, path)
    # TODO Moves the module to the receive point if the point is free.

    # TODO Using the module at the receiving point, if there is a module there.

    moves(path, link)
    # TODO Moves a module back home if it finds it where it was left.

    # TODO return result
