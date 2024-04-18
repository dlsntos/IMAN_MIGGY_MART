from colorama import Fore
import colorama
import os

class Display:
    #function to generate color
    def print_c(self, text, color):# changes color of a single line of string
        colorama.init()# this function is used to initialize the colorama package and for the colors to appear in the exe file
        colored_text = getattr(Fore, color.upper()) + text + colorama.Fore.RESET
        print(colored_text)

    def clear_screan(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def logo(self):
        colorama.init()#this function is used to initialize the colorama package and for the colors to appear in the exe file
        logo = f"""{Fore.CYAN}
        ███╗░░░███╗██╗░██████╗░░██████╗░██╗░░░██╗  ███╗░░░███╗░█████╗░██████╗░████████╗
        ████╗░████║██║██╔════╝░██╔════╝░╚██╗░██╔╝  ████╗░████║██╔══██╗██╔══██╗╚══██╔══╝
        ██╔████╔██║██║██║░░██╗░██║░░██╗░░╚████╔╝░  ██╔████╔██║███████║██████╔╝░░░██║░░░
        ██║╚██╔╝██║██║██║░░╚██╗██║░░╚██╗░░╚██╔╝░░  ██║╚██╔╝██║██╔══██║██╔══██╗░░░██║░░░
        ██║░╚═╝░██║██║╚██████╔╝╚██████╔╝░░░██║░░░  ██║░╚═╝░██║██║░░██║██║░░██║░░░██║░░░
        ╚═╝░░░░░╚═╝╚═╝░╚═════╝░░╚═════╝░░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░\n{Fore.RESET}"""
        print(logo)

    def start_menu(self):
        colorama.init()
        menu = (f"{Fore.BLUE}"
               f"[1] Customer\n"
               f"[2] Manager\n"
               f"[3] Exit\n"
               f"--------------------------------"
               f"{Fore.RESET}")
        print(menu)

    def registration_menu(self):
        colorama.init()
        menu =(f"{Fore.BLUE}"
               f"[Customer Registration]\n\n"
               f"[1] Register\n"
               f"[2] Login\n"
               f"--------------------------------"
               f"{Fore.RESET}")
        print(menu)

    def customer_menu(self):
        menu = (f"{Fore.BLUE}"
                f"\nCustomer Cart:"
                f"\n[1] Add to Cart"
                f"\n[2] Remove from Cart"
                f"\n[3] Display Cart"
                f"\n[4] Checkout\n"
                f"\nGrocery Items:"
                f"\n[5] Search by category"
                f"\n[6] Display items for sale"
                f"\n[7] Exit Program\n"
                f"--------------------------------"
                f"{Fore.RESET}")
        print(menu)

    def manager_menu(self):
        menu =(f"{Fore.BLUE}"
               f"\n[ Miggy Mart ADMIN ACCESS !!! ]\n"
               f"[1] Add item to inventory\n"
               f"[2] Remove Expired Item\n"
               f"[3] Update Item Prices\n"
               f"[4] Exit\n"
               f"--------------------------------"
               f"{Fore.RESET}")
        print(menu)