# 
# ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗      ██████╗
# ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝     ██╔════╝
# ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝█████╗██║     
# ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗╚════╝██║     
# ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗     ╚██████╗
# ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝      ╚═════╝    
# TODO ADD REPO
#

import os
import sys

from colorama import Fore, init

if "win" in sys.platform.lower():
    import msvcrt
else:
    import termios
    import tty
    original_stdin_settings = termios.tcgetattr(sys.stdin)

affirmative_choice = ["y", "Y", "yes", "s", "sim", "yeah", "yah", "ya"]  # affirmative choices, user input detection
negative_choice = ["n", "no", "nao", "na", "nop", "nah"]  # negative choices, user input detection

class Color:
    """
    Return text with color using colorama.
    Pretty much straight forward to read.
    Just use Color().wantedColorOrBold(textToBeColoredOrBolded).
    """
    def __init__(self):
        self.RED = Fore.RED
        self.YELLOW = Fore.YELLOW
        self.BLUE = Fore.BLUE
        self.GREEN = Fore.GREEN
        self.BOLD = '\033[1m'
        self.END = '\033[0m'

    def red(self, text):
        return self.RED + text

    def yellow(self, text):
        return self.YELLOW + text

    def blue(self, text):
        return self.BLUE + text

    def green(self, text):
        return self.GREEN + text

    def bold(self, text):
        return self.BOLD + text + self.END


class Matrix:
    def __init__(self) -> None:
        self.isUpper = None
        self.characters_dict = {
            "a" : 1,
            "b" : 2,
            "c" : 3,
            "d" : 4,
            "e" : 5,
            "f" : 6,
            "g" : 7,
            "h" : 8,
            "i" : 9,
            "j" : 10,
            "k" : 11,
            "l" : 12,
            "m" : 13,
            "n" : 14,
            "o" : 15,
            "p" : 16,
            "q" : 17,
            "r" : 18,
            "s" : 19,
            "t" : 20,
            "u" : 21,
            "v" : 22,
            "w" : 23,
            "x" : 24,
            "y" : 25,
            "z" : 26,
            " " : 27
        }

    def caseTest(self, string):
        # TODO, check each char and save it's casing
        # do this shit later on, first put something at the begginning telling to fuck off
        pass
    
    def stringToList(self, msg):
        r_list = []
        for char in msg:
            r_list.append(char.lower())
        return r_list

    def stringListToMatrixList(self, string_list):
        new_list = []
        for i in string_list:
            new_list.append(self.characters_dict[i.lower()])
        return new_list

def clear():
    """
    check if the machine is windows or linux,
    then clear the screen
    :return: a clean screen :)
    """

    if "win" in sys.platform.lower():
        os.system('cls')

    else:
        os.system('clear')

def show_menu():
    """
    function that prints the main menu options
    :return: menu banner with options
    """
    print(color.red(color.bold("  ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗      ██████╗")))
    print(color.red(color.bold("  ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝     ██╔════╝")))
    print(color.red(color.bold("  ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝█████╗██║     ")))
    print(color.red(color.bold("  ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗╚════╝██║     ")))
    print(color.red(color.bold("  ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗     ╚██████╗")))
    print(color.red(color.bold("  ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝      ╚═════╝")))                                                          
    print("             by " + color.red(color.bold("brunao das marmita")))
    print(color.yellow(color.bold("option number")) + ") option description  " +
          color.red(color.bold("|")) + "  ")
 
def wait_input():
    """
    this function will detect any key press, until that happens, the program will wait
    """
    print("Press " + color.yellow(color.bold("any key")) + " to continue...")
    if "win" in sys.platform.lower():
        while True:
            if msvcrt.kbhit():
                clear()
                break
    else:
        tty.setcbreak(sys.stdin)  # set "stdin" in raw mode, no line buffering from here
        user_input = None  # used to control while loop, the user input will be None,
        # if the user input changes, the while loop should be broken
        while user_input is None:  # while the user input is None (e.i. no key press detect on "stdin"), wait...
            user_input = sys.stdin.read(1)[0]  # this will be reading "stdin" until a key is detected
            clear()  # this will only be reached when a key is detected, until that happens, this will not be reached
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, original_stdin_settings)
        # set "stdin" to default (no raw input)

def exit_func():
    """
    this function should be called when exiting, first clear the screen, then exit
    :return: exits program and clear the screen
    """

    clear()
    sys.exit(0)


if __name__ == "__main__":
    init(autoreset=True)

    # init instances
    matrix = Matrix()
    color = Color()

    # vars
    upperCase = None
    msg = "FUVEST"
    a = [3, 2, 1, 1]
    b = [1, -2, -1, 3]
    
    
    string_list = matrix.stringToList(msg)
    matrix_list = matrix.stringListToMatrixList(string_list) 
    print(string_list)
    print(matrix_list)

    while True:
        clear()
        show_menu()  # show menu
        choice = input(">:")  # wait for user input

        if choice == "":
            clear()
            continue

        try:
            choice = int(choice)  # try to convert choice(str) to choice(int),
            # this is needed because the normal input is a str

        except ValueError:  # if the int() parser cant convert, raises a ValueError, this take care if it
            if choice.lower() == " ":
                continue

            elif choice.lower() == " ":
                continue

            else:  # if user type something that is not an option, ignore and wait for another input
                clear()
                wait_input()
                continue

        if choice == 1:
            exit_func()

        elif choice == 2:
            exit_func()

        elif choice == 0:
            exit_func()
        else:
            clear()
            wait_input()    
