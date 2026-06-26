def example():

    n = int(input("Enter a natural number: "))

    total = 0
    i =  1

    while i <= n:
        total += i
        i += 1

    print(f"sum = {total}")
example()