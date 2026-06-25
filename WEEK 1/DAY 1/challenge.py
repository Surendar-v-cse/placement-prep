def challenge():
    
    name = input("Student name: ")
    nos = int(input("Enter no of subjects: "))

    total_mark = 0
    for i in range (0,nos):
        total_mark += int(input(f"Enter mark for subject {i+1} (out of 100): "))
    
    average = total_mark / nos
    percent = (total_mark / (nos * 100)) * 100

    print(f"""
Student name : {name}

Total mark : {total_mark} / {nos * 100}
Average mark : {average:.2f}
Percent : {percent:.2f}%""")

challenge()