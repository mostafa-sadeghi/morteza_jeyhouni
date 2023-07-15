# import turtle
#
# turtle.shape('turtle')
# turtle.shapesize(2,2)
# sides = int(turtle.textinput('user input','How many sides do you want?'))
#
# for i in range(sides):
#     turtle.forward(100)
#     turtle.left(360/sides)
#
#
# turtle.done()


# a = 4
# b = 5
# #
# if a == b:
#     print("a and b are both equal")
#     print("another")
# #
# # print("outside")
# #
# if a > b:
#     print("a is greater than b")
# if a < b:
#     print("a is less than b")
#
# if a >= b:
#     print("a is greater than or equal to b")
# if a <= b:
#     print("a is greater than or equal to b")
# if a != b:
#     print("a and b are not equal")


# string1 = "amir"
# string2 = "baran"
#
# if string1 > string2:
#     print("string1 is grater than string2")
#
# else:
#     print("string1 is less than string2")


# a = 3
# b = 4
# c = 6

# if a > b and a > c:
#     print("a is the greatest")
# elif b > a and b > c:
#     print("b is the greatest")
# else:print("c is the greatest")


# if a > b or a > c:
#     print("a is greater than b or c")


# name = input("Enter student's name: ")
# score_1 = float(input("enter first score: "))
# score_2 = float(input("enter second score: "))
# score_3 = float(input("enter third score: "))
#
# average = (score_1 + score_2 + score_3)/3
# TODO برنامه ای بنویس که در صورتی که معدل دانش آموز از 90 بالاتر
# باشد، A را پرینت نماید
# اگر معدل او بین 80 تا 90 باشد، B را پرینت نماید
# اگر معدل او بین 70 تا 80 باشد، C
# در غیر  اینصورت D را پرینت نماید



# a = True
# if a:
#     print("a is True")
#
# if a == True:
#     print("a is True")
#
# b = False
# if not b:
#     print("b is False")


# user_name = input("enter the username: ")
# if user_name:
#     print(f"you entered the username:{user_name}")
#
# else:
#     print("username is empty!!!")


# if -1:
#     print("ok")




# USERNAME = "admin"
# PASSWORD = "123"
#
# user_name = input("enter the user name: ").lower()
# if not user_name:
#     print("username is empty")
# else:
#     password = input("enter the password: ").lower()
#     if password:
#         print("username and password are not empty")
#         if user_name == USERNAME and password == PASSWORD:
#             print("valid user.")
#             print("welcome")
#             print("login success")
#         else:
#             print("username or password is not correct...")
#
#     else:
#         print("password is empty")



for i in range(5):
    print("welcome to pygame class",i)
