import math

def area_circle(rad):

    result = int(math.pi * rad ** 2)

    print(f"Area = {result} sqcm")

r = float(input("enter radius of circle"))
area_circle(r)