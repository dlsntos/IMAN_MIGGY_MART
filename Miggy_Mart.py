from Display import Display
from Menu import Menu
import winsound
import time
menu = Menu()
delay = 1.2 
winsound.PlaySound("music.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
display = Display()

while True:
    #calls the start menu function
    display.start_menu()
    try:
        #program asks user to choose a mode
        user = int(input("\nEnter choice here: "))

        #input validation when choice is out of range
        if user < 1 or user > 3:
            display.print_c("\n!Out of range please try again","red")
            time.sleep(delay)
            display.clear_screan()
            continue
        while True:
            try:
                #when user choose customer mode
                if user == 1:
                    menu.customer()
                #when user choose manager mode
                elif user == 2:
                    menu.manager()
                #when user exits program
                elif user == 3:
                    print("Thank you for using our program!")
                    exit()
            except ValueError:
                display.print_c("\n!Enter a valid value","red")
                time.sleep(delay)
                display.clear_screan()
    except ValueError:
        display.print_c("\n!Enter a valid value","red")
        time.sleep(delay)
        display.clear_screan()