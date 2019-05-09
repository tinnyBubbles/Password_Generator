def append_file(password, file_path):
    try:
        password_file = open(file_path, "a+")
        password_file.write(password + "\r\n")
        password_file.close()
    except PermissionError as Err:
        print("Error creating file: {}".format(Err))



