       # VERSION 1
import time
current_time = time.time()
def speed_calc_decorator(func):
    def wrapper():
        func()
        print(time.time() - current_time)
        print(f"{func.__name__}\n\n\n")
    return wrapper        
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
fast_function()
slow_function()


#        # VERSION 2
# import time
# current_time = time.time()
# def speed_calc_decorator(func):
#     def wrapper():
#         func()
#         print(time.time() - current_time)
#         print(f"{func.__name__}\n\n\n")
#     return wrapper()        
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i


#        # VERSION 3
# import time
# current_time = time.time()
# def speed_calc_decorator(func):
#         func()
#         print(time.time() - current_time)
#         print(f"{func.__name__}\n\n\n")        
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i

