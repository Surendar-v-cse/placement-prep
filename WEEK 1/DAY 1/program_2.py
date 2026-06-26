<<<<<<< HEAD
def simple_calculator():
    a = int(input("enter a : "))
    b = int(input("enter b : "))

    op = str(input("Select operator (+,-,*,/) : "))

    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        if b != 0:
            print(a/b)
        else:
            print("Error")
=======
def simple_calculator():
    a = int(input("enter a : "))
    b = int(input("enter b : "))

    op = str(input("Select operator (+,-,*,/) : "))

    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        if b != 0:
            print(a/b)
        else:
            print("Error")
>>>>>>> 014bb9916ed1e33dcb64c7d027a58547370437d2
simple_calculator()