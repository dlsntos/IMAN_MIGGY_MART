from colorama import Fore
import colorama
import os

class Display:
    #this function changes the color of a single line of string
    def print_c(self, text, color):
        #colorama.init() is used to initialize the colorama package and for the colors to appear in the exe file
        colorama.init()
        colored_text = getattr(Fore, color.upper()) + text + colorama.Fore.RESET
        print(colored_text)

    #this function clears the previous output and makes the system look clean and not cluttered
    def clear_screan(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    #this function stores the official logo of our system
    def logo(self):
        colorama.init()
        logo = f"""{Fore.CYAN}
        ███╗░░░███╗██╗░██████╗░░██████╗░██╗░░░██╗  ███╗░░░███╗░█████╗░██████╗░████████╗
        ████╗░████║██║██╔════╝░██╔════╝░╚██╗░██╔╝  ████╗░████║██╔══██╗██╔══██╗╚══██╔══╝
        ██╔████╔██║██║██║░░██╗░██║░░██╗░░╚████╔╝░  ██╔████╔██║███████║██████╔╝░░░██║░░░
        ██║╚██╔╝██║██║██║░░╚██╗██║░░╚██╗░░╚██╔╝░░  ██║╚██╔╝██║██╔══██║██╔══██╗░░░██║░░░
        ██║░╚═╝░██║██║╚██████╔╝╚██████╔╝░░░██║░░░  ██║░╚═╝░██║██║░░██║██║░░██║░░░██║░░░
        ╚═╝░░░░░╚═╝╚═╝░╚═════╝░░╚═════╝░░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░\n{Fore.RESET}"""
        print(logo)

    #this function stores the starting menu screen display
    def start_menu(self):
        colorama.init()
        menu = (f"{Fore.BLUE}"
               f"[1] Customer\n"
               f"[2] Manager\n"
               f"[3] Exit\n"
               f"--------------------------------"
               f"{Fore.RESET}")
        self.logo()
        print(menu)

    # this function stores the registration and login menu display for customers
    def registration_menu(self):
        colorama.init()
        self.logo()
        menu =(f"{Fore.BLUE}"
               f"[Customer Registration]\n\n"
               f"[1] Register\n"
               f"[2] Login\n"
               f"--------------------------------"
               f"{Fore.RESET}")
        print(menu)

    #this function stores the main customer menu display
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
        self.logo()
        print(menu)

    # this function stores the Manager menu display
    def manager_menu(self):
        menu =(f"{Fore.BLUE}"
               f"\n[ ADMIN ACCESS !!! ]\n"
               f"[1] Add item to inventory\n"
               f"[2] Remove Expired Item\n"
               f"[3] Update Item Prices\n"
               f"[4] Exit\n"
               f"--------------------------------"
               f"{Fore.RESET}")
        self.logo()
        print(menu)