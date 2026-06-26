def swapping():
    a = input()
    b = input()
    print(f"\nBefore swapping : A = {a} , B = {b}")
    a,b = b,a
    print(f"\nAfter swapping : A = {a} , B = {b}")
swapping()