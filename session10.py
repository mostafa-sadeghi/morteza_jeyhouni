# for i in range(5):
#     print("hi")
#
#
# i = 0
# while i < 5:
#     print("hi")
#     i += 1

# TODO
"""
کشیدن مربع و پنجضلعی

with for loop
and with while

"""


# quit = "n"
# while quit == "n":
#     quit = input("Do you want to quit? ")

#
# done = False
# while not done:
#     quit = input("Do you want to quit? ")
#     if quit == "y":
#         done = True
#
#     attack = input("Does your elf attack the dragon? ")
#     if attack == "y":
#         print("bad choice, you died.")
#         done = True


# import random
# for i in range(50):
#     my_number = random.randrange(50)
#     print(my_number)
# for i in range(50):
#     my_number = random.randint(1,50)
#     print(my_number)
#
#
# numbers = [1,2,3,4,5,6,7,8,9]
# print(random.choice(numbers))
#
# print(numbers[random.randrange(len(numbers))])

# from random import choice
#
# options = ["r", "p", "s"]
# result = {'user': 0, 'system': 0}
# while True:
#     user_choice = input("Enter your choice ('r', 'p', 's'): ")
#     while user_choice not in options:
#         user_choice = input("Enter your choice ('r', 'p', 's'): ")
#
#     system_choice = choice(options)
#
#     if (user_choice == "p" and system_choice == "r") or (user_choice == "s" and system_choice == "p") \
#             or (user_choice == "r" and system_choice == "s"):
#         print("system's choice is : ", system_choice)
#         print("user is the winner.")
#         result['user'] += 1
#     elif user_choice == system_choice:
#         print("system's choice is : ", system_choice)
#         print("equal")
#     else:
#         print("system's choice is : ", system_choice)
#         print("system is the winner!")
#         result['system'] += 1
#     user_input = input("Do you want to quit('y' or 'n'): ")
#     if user_input == 'y':
#         print("#"*20)
#         print("user's score:", result['user'])
#         print("system's score:", result['system'])
#         break


# def my_function(name, family):
#     return f"Hello {name} {family}"
#
#
# result = my_function("arshin", "rezaei")
# print(result)
# print(my_function("milad","blalallalal"))
#
# name = input("enter your name: ")
# family = input("enter your family: ")
# print(my_function(name, family))


def add():
    number1 = input("Enter a number: ")
    number2 = input("Enter a number: ")
    if number1.isdecimal():
        number1 = int(number1)
    else:
        return f"{number1} is not a number"

    if number2.isdecimal():
        number2 = int(number2)
    else:
        return f"{number2} is not a number"

    return  f"result is :{number1 + number2}"

print(add())