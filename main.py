import gen_rand_password as gen
from tkinter import *


def exit():
    """
    Exits the program
    """

    return True


def generate_password(length):
    '''
    Returns a randomly generated string of int length
    '''

    return gen.gen_rand_password(length)


def build_gui():
    window = Tk()
    window.geometry('1000x100')
    window.title("Password Generator")

    lbl = Label(window, text='password')

    btn_generate = Button(window, text='Generate Password')
    lbl.pack()
    btn_generate.pack()

    return window



if __name__ == '__main__':

    gui = build_gui()
    gui.mainloop()
