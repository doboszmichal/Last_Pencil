import random
CHAR = "|"
user = ""


def start():
    pencils = get_pencils()
    get_users()
    print_pencils(int(pencils))


def get_pencils():
    print("How many pencils would you like to use:")
    pencils = input()
    while not pencils.lstrip("-").isnumeric() or int(pencils) <= 0:
        if not pencils.lstrip("-").isnumeric():
            print("The number of pencils should be numeric")
        else:
            print("The number of pencils should be positive")
        pencils = input()
    return pencils


def get_users():
    global user
    print("Who will be the first (John, Jack)")
    user = input()
    while user not in ("John", "Jack"):
        print("Choose between 'John' and 'Jack'")
        user = input()
    return user



def print_pencils(pencils):
    global user
    pencils_num = pencils
    print(CHAR * int(pencils_num))
    while pencils > 0:
        if user == "John":
            print("John's turn:")
            selected_pencils = input()
            user = "Jack"
        else:
            selected_pencils = 0
            print("Jack's turn!")
            if pencils_num % 4 == 0:
                selected_pencils = 3
                print(selected_pencils)
                user = "John"
            elif pencils_num == 1:
                selected_pencils = 1
                print(selected_pencils)
                user = "John"
            elif pencils_num % 4 == 1:
                selected_pencils = random.randint(1, 3)
                print(selected_pencils)
                user = "John"
            elif pencils_num % 4 == 2:
                selected_pencils = 1
                print(selected_pencils)
                user = "John"
            elif pencils_num % 4 == 3:
                selected_pencils = 2
                print(selected_pencils)
                user = "John"

        while str(selected_pencils) not in ("1", "2", "3"):
            print("Possible values: '1', '2', '3'")
            selected_pencils = input()
        while int(selected_pencils) > pencils_num:
            print("Too many pencils were taken")
            selected_pencils = int(input())
        pencils_num = pencils_num - int(selected_pencils)
        if pencils_num == 0:
            if user == "John":
                print("John won!")
            else:
                print("Jack won!")
            exit()
        else:
            print(CHAR * pencils_num)


start()
