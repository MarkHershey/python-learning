# lets say you have a function
# that says hello
def hello(name: str):
    print(f"Hello, {name}")


# you have another function
# that prints the current temperature
def printTemp(temp: float):
    print("Current Temperature: {:.2f}".format(temp))


# now lets try to call them
# and see how it looks like
hello("Mark")
printTemp(23.5)

"""
You already have these two functions
and probablly more functions that are similar to these two,
which prints small pieces of information to the user

Now, you want to present the information more nicely,
so you have to decided that whenever you show the info,
it will be wrapped with -------------- this kind of line breakers
"""

# you can rewrite the function
def hello_2(name: str):
    print("-------------------------------\n")
    print(f"Hello, {name}")
    print("\n-------------------------------\n")


hello_2("Mark")
"""
'hello_2' should work as expected
but you have to modify all of your small functions to
achieve a consistent look

so you have decided to write a function
that just helps you to print the line breakers
before and after you call any info functions
"""


def wrap_with_line_breakers(func, func_arg):
    print("-------------------------------\n")
    func(func_arg)
    print("\n-------------------------------\n")


wrap_with_line_breakers(hello, "Mark")
wrap_with_line_breakers(printTemp, 23.5)

"""
great, now it works
but I don't want to call the function indirectly

what you really want, is a function that helps you modify
your orginal funcions
so that you can have a new function, behaves exactly as what you need

so in python, (and many other languages), you can pass function
as an argument to another function, you can also return a function

generally, functions are called Callables
"""
from typing import Callable


def line_break_decorator(func: Callable) -> Callable:
    def modified_func(arg):
        print("-------------------------------\n")
        func(arg)
        print("\n-------------------------------\n")

    return modified_func


# now you try to use this line_break_decorator
# to modify printTemp
printTemp = line_break_decorator(printTemp)
# yeah now the printTemp has been modified!
# try it:
printTemp(34)


"""
finally, we have to come to what you have been waiting for

what if you want to write a new function that prints weather info

how do you use your existing decorator to decorate your new function?
"""


@line_break_decorator
def printWeather(info: str):
    print(f"Today's weather: {info}")


# try it !!
printWeather("Mostly cloudy")
