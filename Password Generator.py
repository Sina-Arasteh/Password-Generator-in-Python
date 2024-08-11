from random import choice, randint


lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['`', '~', '@', '#', '%', '^', '*', '-', '_', '=', '!', '$', '&', '(', ')', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '/', '"', "'", '<', '>', '?', '.']


password = []
def password_generator():
    for i in range(1, 17):
        random_num = randint(1, 5)
        if random_num == 1:
            l1 = choice(lowercase_letters)
            password.append(l1)
        elif random_num == 2:
            u2 = choice(uppercase_letters)
            password.append(u2)
        elif random_num == 3:
            n3 = choice(numbers)
            password.append(n3)
        else:
            s4 = choice(symbols)
    return "".join(password)


print(password_generator())