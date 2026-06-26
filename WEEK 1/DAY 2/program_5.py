def mul_table():

    n = int(input("Enter a number to see its multiplication table: "))
    m = int(input("Enter no of rows: "))

    for i in range(1,m+1):
        ans = n*i
        print(f"{n} x {i} = {ans}")

mul_table()