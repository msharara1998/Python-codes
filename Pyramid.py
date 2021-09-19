# Elegant Python functions to print some triangular shapes
def pyramid(n):
    for i in range(1, n):
        print(("* "*i).center(2*n-1))


def inverted_pyramid(n):
    for i in range(1, n):
        print(("* "*(n-i)).center(2*n-1))


def right_triangle(n):
    for i in range(1, n):
        print(("*" * i).ljust(2 * n - 1))


def hollow_pyramid(n):
    print("*".center(2*n+3))
    for i in range(n):
        print(("*"+" "*(2*i+1)+"*").center(2*n+3))
    print("* "*(n+2))

