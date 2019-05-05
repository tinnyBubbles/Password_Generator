import gen_rand_password as gen


# Ask user to enter program or exit
enter_Program = input("Enter 'Y' to generate a password or press any key to exit")
enter_Program = enter_Program.lower()


if enter_Program == "y":
    print(gen.gen_rand_password(15))

else:
    exit()
