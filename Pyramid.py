# Elegant Python functions to print some triangular shapes
def pyramid(n):
    for i in range(1, n):
        print(("* "*i).center(2*n-1))


pyramid(23)


def inverted_pyramid(n):
    for i in range(1, n):
        print(("* "*(n-i)).center(2*n-1))


inverted_pyramid(23)