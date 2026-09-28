# 1
# def show_arguments(func):
#     def inner(a, b):
#         print("Arguments:", a, b)
#         return func(a, b)
#     return inner

# @show_arguments
# def multiply(a, b):
#     return a *b

# a = int(input())
# b = int(input())
# print(multiply(a, b))





# 2
# def frame(func):
#     def show_text(text):
#         print (func())
#         print(text)
#         print (func())
#     return show_text
# @frame
# def eee():
#     return "=========="
# eee("Python")
















# 3
# def double_result(func):
#     def get_numbers(number):
#         return func(number)
#     return get_numbers
# @double_result
# def doub(num):
#     return num*2
# print(doub(int(input())))











# 4
# multyply = lambda a, b: a*b
# a = int(input())
# b = int(input())


# print(multyply(a, b))











# 5
# def count_calls(func):
#     n = 0
#     def wrapper():
#         nonlocal n
#         n += 1
#         print("Calls:", n)
#         func()
#     return wrapper
# @count_calls
# def hello():
#     print("Hello")


# hello()
# hello()
# hello()












# 6
# def string_only(func):
#     def inner(value):
#         if type(value) == int:
#             print("A string is required")

#         else:
#             func(value)
#     return inner

# @string_only
# def show(value):
#     print(value)




# show(100)







# # 7
# def string_only(func):
#     def inner(value):
#         if value >=18:
#             func(value)

#         else:
#             print("Access denied")
#     return inner

# @string_only
# def show(value):
#     print("Welcome")




# show(100)










# 8
# pass









# 9
# def add_prefix(func):
#     def get_name(name):
#         return "Result: " + func(name)
#     return get_name
# @add_prefix
# def prefix(name):
#     return name

# print(prefix("Ali"))











# 10
# def check_division(func):
#     def wrapper(a, b):
#         if b == 0 or a==0:
#             print("Cannot divide by zero")
#         else:
#             print(func(a,b))
#     return wrapper

# @check_division
# def divide(a, b):
#     return  a/b

# divide(10, 0)
# divide(10, 2)









# 11
# loc = []
# add = lambda licy: [loc.append(i) for i in licy if i>0]

# add([-4,7,0,-2,9,3])


# print(loc)











# add = lambda a, b : a+b
# minus = lambda a, b : a-b
# zarb = lambda a, b : a*b
# taksim = lambda a, b : a/b




# def show_start(func):
#     def operating():
#         print(func)
    