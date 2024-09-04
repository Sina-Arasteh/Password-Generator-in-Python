from random import choice, randint
import string

characters = string.ascii_letters + string.digits + string.punctuation

len_of_password = int(input("Enter the length of your desired password: "))
password = []

def password_generator():
    for i in range(1, len_of_password+1):
        password.append(choice(characters))
    return "".join(password)


print(password_generator())
