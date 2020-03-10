from control import Control
import tkinter as tk
import time

port = "COM5"
cont = Control(port)


def forward(event):
    cont.send("1")


def back(event):
    cont.send("0")


def stop(event):
    cont.send("!")


def quit_app():
    exit()


def do_stuff(event):
    print(event)
    print("down")


def do_things(event):
    print(str(event))
    print("up")


class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill="both", expand=1)
        forward_button = tk.Button(self, text="forward")
        forward_button.place(x=0, y=0)
        forward_button.bind('<ButtonPress-1>', forward)
        forward_button.bind('<ButtonRelease-1>', stop)

        reverse_button = tk.Button(self, text="reverse")
        reverse_button.place(x=0, y=60)
        reverse_button.bind('<ButtonPress-1>', back)
        reverse_button.bind('<ButtonRelease-1>', stop)

        quit_button = tk.Button(self, text="quit", command=quit_app)
        quit_button.place(x=250, y=400)

        test_button = tk.Button(self, text="test")
        test_button.pack(side="right")
        test_button.bind('<ButtonPress-1>', do_stuff)
        test_button.bind('<ButtonRelease-1>', do_things)


def main():
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Car Controller")
    root.configure(bg='red')

    app = Window(root)

    root.mainloop()


main()
