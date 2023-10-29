sweets = int(input("How many sweets? "))
students = int(input("How many students? "))
sweet = "sweets" if (sweets//students) > 1 else "sweet"
print(f"Give each student {sweets//students} {sweet} with {sweets % students} left over.")
