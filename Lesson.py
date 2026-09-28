# def print_welcome(func):
#     def inner(name):
#         print("Welcome")
#         return func(name)
#     return inner

# @print_welcome
# def hello(name):
#     return name


# print(hello("Ali"))




# def print_welcome(func):
#     def inner(name):
#         print(func(name))
#         print("Goodbay")
        
#     return inner

# @print_welcome
# def hello(name):
#     return name


# hello("Dushanbe")









# def chicl(n):
#     def print_welcome(func):
#         def inner(name):
#             for _ in range(n):
#                  func(name)
#         return inner
#     return print_welcome

# @chicl(3)
# def hello(name):
#     print(name)


# hello("Dushanbe")











# def show_funcion_name(func):
#     def addddddddd(a, b):
#         print("Funcion:", "add")
#         func(a, b)
#     return addddddddd
# @show_funcion_name
# def add(a, b):
#     print(a+b)



# a = int(input())
# b = int(input())

# add(a, b)





# def uppercase_result(func):
#     def get_name(name):
#         res = func(name)
#         return res.upper()
#     return get_name

# @uppercase_result
# def get_nname(name):
#     return name


# print(get_nname("Ali"))










# def positive_number(func):
#     def squaer(a):
#         return(func(a))
#     return squaer
# @positive_number
# def check_number(a):
#     if a>0:
#         print(a*a)
#     else:
#         print('The number must be positive')

# check_number(-5)










# add = lambda a, b: a+b
# print(add(7, 5))









# add = lambda a: a*a
# print(add(6))







# lict = [1,2,3,4,5,6]

# filter = lambda list: [i for i in list if i%2==0]



# print(filter(lict))





# dic = {
#     "Ali":22,
#     "Sara":19,
#     "Bob":25
# }

# sorted = lambda dict, max1=-999999: [(i, b) for i,b in dict.items()]


# print(sorted(dic))










