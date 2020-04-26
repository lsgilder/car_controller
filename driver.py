from control import Control
import tkinter as tk
import time

# port = "COM5"
# cont = Control(port)


# These functions use the control class to send data through the com port
def forward(event):
    cont.send("1")


def back(event):
    cont.send("0")


def leftu(event):
    cont.send("3")


def leftd(event):
    cont.send("5")


def rightu(event):
    cont.send("4")


def rightd(event):
    cont.send("4")


def stop(event):
    cont.send("!")


def quit_app():
    exit()


class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.master = master
        self.init_window()

    # Creates the buttons on the gui
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill="both", expand=1)
        forward_button = tk.Button(self, text="forward")
        forward_button.place(relx=0.5, rely=0.45, anchor="center")
        forward_button.bind('<ButtonPress-1>', forward)
        forward_button.bind('<ButtonRelease-1>', stop)

        reverse_button = tk.Button(self, text="reverse")
        reverse_button.place(relx=0.5, rely=0.55, anchor="center")
        reverse_button.bind('<ButtonPress-1>', back)
        reverse_button.bind('<ButtonRelease-1>', stop)

        left_button = tk.Button(self, text="front left")
        left_button.place(relx=0.38, rely=0.45, anchor="center")
        left_button.bind('<ButtonPress-1>', leftu)
        left_button.bind('<ButtonRelease-1>', stop)

        left_button = tk.Button(self, text="back left")
        left_button.place(relx=0.38, rely=0.55, anchor="center")
        left_button.bind('<ButtonPress-1>', leftd)
        left_button.bind('<ButtonRelease-1>', stop)

        right_button = tk.Button(self, text="front right")
        right_button.place(relx=0.62, rely=0.45, anchor="center")
        right_button.bind('<ButtonPress-1>', rightu)
        right_button.bind('<ButtonRelease-1>', stop)

        right_button = tk.Button(self, text="back right")
        right_button.place(relx=0.62, rely=0.55, anchor="center")
        right_button.bind('<ButtonPress-1>', rightd)
        right_button.bind('<ButtonRelease-1>', stop)

        quit_button = tk.Button(self, text="quit", command=quit_app)
        quit_button.place(relx=0.5, rely=0.9, anchor="center")


def main():
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Car Controller")
    root.configure(bg='red')

    app = Window(root)

    root.mainloop()


main()
