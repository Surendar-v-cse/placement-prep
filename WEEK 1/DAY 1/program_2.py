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
simple_calculator()