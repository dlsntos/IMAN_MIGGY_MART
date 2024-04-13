from colorama import Fore
import colorama
import os

class Display:
    #function to generate color
    def print_colored(self,text, color):
        colorama.init()#this function is used to initialize the colorama package and for the colors to appear in the exe file
        colored_text = getattr(Fore, color.upper()) + text + colorama.Fore.RESET
        print(colored_text)

    def clear_screan(self):#cleae screen after output
        os.system('cls' if os.name == 'nt' else 'clear')