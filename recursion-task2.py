
n = int(input("Please enter any number of your choices:  "))     # prompting the user to input a figure of choice


# defining a function
def fibonacci(n):
    if n < 0:
        return "please provide a figure that is >= 0"
    elif n == 0:
        return 0
    elif n < 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# calling a function
print("The fibonacci of the above figure is", fibonacci(n))
