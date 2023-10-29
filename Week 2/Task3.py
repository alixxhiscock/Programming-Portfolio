students = int(input(f"How many students? "))
groupsize = int(input(f"Required group size? "))
print(f"There will be {students//groupsize} groups with {students % groupsize} students left over.")