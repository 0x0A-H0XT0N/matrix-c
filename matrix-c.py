# 
# ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗      ██████╗
# ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝     ██╔════╝
# ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝█████╗██║     
# ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗╚════╝██║     
# ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗     ╚██████╗
# ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝      ╚═════╝    
# https://gitlab.com/h0xt0n/matrix-c
#

import os
import sys
from time import sleep
from types import SimpleNamespace

import numpy as np
from colorama import Fore, init

# if "win" in sys.platform.lower():
#     import msvcrt
# else:
#     import termios
#     import tty
#     original_stdin_settings = termios.tcgetattr(sys.stdin)

characters_dict = {
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
        

    def twoBytwo_verifier(self, matrix):
        size = 0
        """[summary]
        verifies if a matrix is a two by two
        Returns:
            [type]: [description]
        """        
        try:
            for l in matrix:
                size += len(l)
            if size != 4:
                return False
            return True
        except:
            return False

    def caseTest(self, string):
        for s in string:
            if s.isupper():
                return True
        return False
    
    def split_list(self, lst):
        half = len(lst)//2
        return lst[:half], lst[half:]
    
    def stringToList(self, msg):
        r_list = []
        for char in msg:
            r_list.append(char.lower())
        return r_list

    def stringListToIntList(self, string_list):
        new_list = []
        for i in string_list:
            new_list.append(characters_dict[i.lower()])
        return new_list
    
    def intListToMatrix(self, int_list):
        if len(int_list) % 2 != 0:
            int_list.append(0)
        upper_bound, lower_bound = self.split_list(int_list)
        matrix = [upper_bound, lower_bound]
        return matrix
    
    def matrix_multiplier(self, m1, m2):
        """[summary]
        multiplies encoder matrix X msg to be encoded, handles error if multiplication cannot happen
        Args:
            m1 ([type]): nested list (matrix) [description] encoder matrix
            m2 ([type]): nested list (matrix) [description] msg to be encoded
        """        
        try:
            return np.dot(m1, m2)
        except ValueError as e:
            print(color.red(color.bold("Erro. Trace:")))
            print(e)
            wait_input()
            return False
    
    def inverse_matrix(self, matrix):
        try:
            return np.linalg.inv(matrix)
        except ValueError as e:
            print(color.red(color.bold("Erro. Trace:")))
            print(e)
            wait_input()
            return False
    
    def multiply(self, encoder, msg):
        if not self.twoBytwo_verifier(encoder):
            print(color.red(color.bold("Erro. ")) + "Matriz codificadora não é 2x2.")
            wait_input()
            return
        if msg == None or "" or " ":
            clear()
            print("Permitido apenas letras de a-z e espaço na mensagem original. " +
                  "Proibido números, caracteres especiais ou com acento.")
            wait_input()
            return
        if self.caseTest(msg):
            # clear()
            # print("Aviso: caracteres maiúsculos serão convertidos em minúsculos.")
            # wait_input()
            msg = msg.lower()
        for char in msg:
            if char not in characters_dict:
                clear()
                print("Permitido apenas letras de a-z e espaço na mensagem original. " +
                      "Proibido números, caracteres especiais ou com acento.")
                wait_input()
                return
        string_list = self.stringToList(msg)
        int_list = self.stringListToIntList(string_list)
        matrix_list = self.intListToMatrix(int_list)
        encoded_matrix_msg = self.matrix_multiplier(encoder, matrix_list)
        decoder = self.inverse_matrix(encoder)
        return encoded_matrix_msg, decoder
        
        
def clear():
    """
    clears the screen based on OS type
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
    print()
    print(color.red(color.bold("  ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗      ██████╗")))
    print(color.red(color.bold("  ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝     ██╔════╝")))
    print(color.red(color.bold("  ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝█████╗██║     ")))
    print(color.red(color.bold("  ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗╚════╝██║     ")))
    print(color.red(color.bold("  ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗     ╚██████╗")))
    print(color.red(color.bold("  ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝      ╚═════╝")))                                                          
    print("             by " + color.red(color.bold("brunao das marmita")))
    print(color.red(color.bold("--------------------------------------------------------------"))) 
    
# def wait_input():
#     """
#     this function will detect any key press, until that happens, the program will wait
#     """
#     print("Pressione " + color.yellow(color.bold("qualquer tecla")) + " para continuar...")
#     if "win" in sys.platform.lower():
#         while True:
#             if msvcrt.kbhit():
#                 clear()
#                 break
#     else:
#         tty.setcbreak(sys.stdin)  # set "stdin" in raw mode, no line buffering from here
#         user_input = None  # used to control while loop, the user input will be None,
#         # if the user input changes, the while loop should be broken
#         while user_input is None:  # while the user input is None (e.i. no key press detect on "stdin"), wait...
#             user_input = sys.stdin.read(1)[0]  # this will be reading "stdin" until a key is detected
#             clear()  # this will only be reached when a key is detected, until that happens, this will not be reached
#         termios.tcsetattr(sys.stdin, termios.TCSADRAIN, original_stdin_settings)
#         # set "stdin" to default (no raw input)

def wait_input():
    input(color.yellow(color.bold("ENTER")) + " para continuar...")
    clear

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
    
    while True:
        input_list = list()
        encoder_matrix_list = list()

        clear()
        show_menu()
        print("Insira a matriz codificadora: ")
        print("[[ " + color.red(color.bold("X")) + "  x]")
        print(" [ x  x]]")
        try:
            n = input(">:")
            int(n)
            input_list.append(n)
        except:
            clear()
            wait_input()
            continue

        clear()
        show_menu()
        print("Insira a matriz codificadora: ")
        print("[[ " + input_list[0] + "  "   + color.red(color.bold("X")) + "]")
        print(" [ x  x]]")
        try:
            n = input(">:")
            int(n)
            input_list.append(n)
        except:
            clear()
            wait_input()
            continue

        clear()
        show_menu()
        print("Insira a matriz codificadora: ")
        print("[[ " + input_list[0] + "  " + input_list[1] + "]")
        print(" [ " + color.red(color.bold("X")) + "  x]]")
        try:
            n = input(">:")
            int(n)
            input_list.append(n)
        except:
            clear()
            wait_input()
            continue

        clear()
        show_menu()
        print("Insira a matriz codificadora: ")
        print("[[ " + input_list[0] + "  " + input_list[1] + "]")
        print(" [ " + input_list[2] + "  " + color.red(color.bold("X")) + "]]")
        try:
            n = input(">:")
            int(n)
            input_list.append(n)
        except:
            clear()
            wait_input()
            continue

        upper_bound = "[[ " + str(input_list[0]) + "  " + str(input_list[1]) + "]"
        lower_bound = " [ " + str(input_list[2]) + "  " + str(input_list[3]) + "]]"
        for n in input_list:
            encoder_matrix_list.append(int(n))
        upper_matrix, lower_matrix = matrix.split_list(encoder_matrix_list)
        del(encoder_matrix_list)
        encoder_matrix_list = list()
        encoder_matrix_list.append(upper_matrix)
        encoder_matrix_list.append(lower_matrix)
        
        clear()
        show_menu()
        print("Matriz codificadora: ")
        print(upper_bound)
        print(lower_bound)
        print(color.red(color.bold("--------------------------------------------------------------"))) 
        print("Mensagem a ser codificada:")
        msg_to_encode = input(">:")
        
        try:
            encoded_matrix_msg, decoder = matrix.multiply(encoder_matrix_list, msg_to_encode)
        except:
            continue
        
        clear()
        show_menu()
        print("Matriz codificadora:")
        print(upper_bound)
        print(lower_bound)
        print(color.red(color.bold("--------------------------------------------------------------")))        
        print("Mensagem criptografada:")
        print(encoded_matrix_msg)
        print(color.red(color.bold("--------------------------------------------------------------")))        
        print("Dicionário numérico:")
        print(characters_dict)
        print(color.red(color.bold("--------------------------------------------------------------")))        
        input((color.red(color.bold("ENTER")) + " para a resolução."))
        
        clear()
        show_menu()
        print("Mensagem descriptografada:")
        print(color.red(color.bold(msg_to_encode)))
        print(color.red(color.bold("--------------------------------------------------------------")))   
        print("Matriz decodificadora (inversa):")
        print(decoder)
        print(color.red(color.bold("--------------------------------------------------------------")))   
        sleep(1)
        wait_input()
        continue
