import threading
from pypresence import Presence
import time
from tkinter import *
from tkinter.ttk import *

# Creating and connecting presence
rpc = Presence(client_id="857867709618061324")
rpc.connect()


def window():
    """
    Tkinter window initialisation
    """

    # Create Object
    root = Tk()

    # Initialize tkinter window with dimensions
    root.geometry('600x500')

    # Create button
    btn = Button(root, text='Click me!',
                 command=lambda: threading.Thread(target=buttonOne).start())

    # Set the position of button on the top of window
    btn.pack(side='top')
    root.mainloop()


def buttonOne():
    """
    Used to call display from thread start
    :return: None
    """
    display()
    return


def display():
    """
    Displays rich presence details
    """
    while True:  # The presence will stay on as long as the program is running
        current_time = int(time.time())
        minutes = 1
        hours_added = current_time + (minutes * 60)
        rpc.update(state="fun", details="playing", end=hours_added,
                   large_image="307485929256211")  # Set the presence
        time.sleep(minutes * 60)  # Sleep for length of end time
        break


if __name__ == "__main__":
    window()
