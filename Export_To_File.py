def append_file(password, file_path):

    password_file = open(file_path, "a+")
    password_file.write(password + "\r\n")
    password_file.close()


password1 = "test"
file_path = "/home/brandon"


append_file(password1, file_path)