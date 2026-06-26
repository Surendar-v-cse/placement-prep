def leap_year():

    year = int(input("Enter the year to be checked is it leap year or not: "))

    if year%4 == 0 and year%100 != 0:
        print(f"{year} is an leap year!!")
    else:
        print(f"{year} is not an leap year!!")
leap_year()