def append_file(password):

    password_file = open("passwords.txt", "a+")
    password_file.write(password + "\r\n")
    password_file.close()
