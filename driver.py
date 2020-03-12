from control import Control
import tkinter as tk
import time

port = "COM5"
cont = Control(port)


def forward(event):
    cont.send("1")


def back(event):
    cont.send("0")


def left(event):
    cont.send("3")


def right(event):
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

        left_button = tk.Button(self, text="left")
        left_button.place(relx=0.4, rely=0.5, anchor="center")
        left_button.bind('<ButtonPress-1>', left)
        left_button.bind('<ButtonRelease-1>', stop)

        right_button = tk.Button(self, text="right")
        right_button.place(relx=0.6, rely=0.5, anchor="center")
        right_button.bind('<ButtonPress-1>', right)
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
