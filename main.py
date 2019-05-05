import gen_rand_password as gen
from tkinter import *


password = "1 "
pass_length = 15


def exit():
    """
    Exits the program
    """

    return True


'''def generate_password():
    
    Returns a randomly generated string of int length
    

    # return gen.gen_rand_password(length)
    global password
    password = gen.gen_rand_password(pass_length)
    '''


class BuildGui:

    def __init__(self, char_length):
        self.password_length = char_length

        self.window = Tk()
        self.window.geometry('1000x100')
        self.window.title("Password Generator")

        self.lbl = Label(self.window, text=password)
        self.btn_generate = Button(self.window, text='Generate Password', command=self.generate_password)

        self.lbl.pack()
        self.btn_generate.pack()
        self.window.mainloop()

    def generate_password(self):
        '''
        Returns a randomly generated string of int length
        '''

        # return gen.gen_rand_password(length)
        global password
        password = gen.gen_rand_password(self.password_length)
        self.lbl.configure(text=password)


if __name__ == '__main__':
    gui = BuildGui(pass_length)
