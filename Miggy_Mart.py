from Display import Display
from Menu import Menu

import winsound
import time

menu = Menu()

t = 1.2 

winsound.PlaySound("music.wav", winsound.SND_LOOP + winsound.SND_ASYNC)

display = Display()

while True:
    display.logo()#testing
    display.start_menu()
    try:
        user = int(input("\nEnter choice here: "))

        if user < 1 or user > 3:
            display.print_c("\n!Out of range please try again","red")
            time.sleep(t)
            display.clear_screan()
            continue
        while True:
            try:
                if user == 1:
                    menu.customer()
                elif user == 2:
                    menu.manager()
                elif user == 3:
                    print("Thank you for using our program!")
                    exit()
            except ValueError:
                display.print_c("\n!Enter a valid value","red")
                time.sleep(t)
                display.clear_screan()
    except ValueError:
        display.print_c("\n!Enter a valid value","red")
        time.sleep(t)
        display.clear_screan()