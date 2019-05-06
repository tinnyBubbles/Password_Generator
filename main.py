import gen_rand_password as gen
from tkinter import *
import Export_To_File as export
from configparser import SafeConfigParser


parser = SafeConfigParser()
parser.read('configuration.ini')

config_path = parser.get('configuration', 'path')
file_name = parser.get('configuration', 'file_name')
path = config_path + file_name
config_pass_length = parser.get('configuration', 'character_length')
pass_length = int(config_pass_length)


class BuildGui:

    def __init__(self, char_length):
        self.password_length = char_length

        self.window = Tk()
        self.window.geometry('1000x100')
        self.window.title("Password Generator")

        self.lbl = Label(self.window, text='')
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
        export.append_file(password, path)
        self.lbl.configure(text="Your password has been created")


if __name__ == '__main__':
    gui = BuildGui(pass_length)
