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


def draw_gui():
    window = Tk()
    window.geometry('1000x100')
    window.title("Password Generator")

    window.mainloop()


if __name__ == '__main__':
    draw_gui()
