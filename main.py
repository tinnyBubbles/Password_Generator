from random import getrandbits

# Ask user to enter program or exit
enter_Program = input("Enter 'Y' to generate a password or press any key to exit")
enter_Program = enter_Program.lower()


# Functions
def gen_rand_password(b_length):
    """Generates a random number of a specified bit length then converts to hex.
       Returns an hex.
    """
    random_hex = hex(getrandbits(b_length))
    return random_hex


def salt(rand_string):
    """inserts random symbols into specified random string.
       returns string
    """


#  Get user input/ bit length of password/ file path to store password

if enter_Program == "y":
    print(gen_rand_password(64))

else:
    exit()
