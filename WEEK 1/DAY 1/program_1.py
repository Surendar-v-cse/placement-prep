def details():
    name = str(input("Name: "))
    age = int(input("Age: "))
    college = str(input("College: "))
    dept = str(input("Dept: "))

    print(f"\nName : {name}",
          f"Age : {age}",
          f"College : {college}",
          f"Dept : {dept}",
          sep = "\n"
          )
details()