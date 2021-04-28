result = int(input("Enter any number: "))   # prompting the user to input any number


#
def fact(n):
    if n < 0:
        return "Please enter a positive number"
    elif n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(result))
