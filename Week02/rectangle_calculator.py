# Calculate area and perimeter from dimensions entered by the user.

length = float(input("Enter the length in metres: "))
width = float(input("Enter the width in metres: "))

area = length * width
perimeter = 2 * (length + width)

print()
print("RECTANGLE CALCULATION")
print("=====================")
print(f"Length: {length:.2f} metres")
print(f"Width: {width:.2f} metres")
print(f"Area: {area:.2f} square metres")
print(f"Perimeter: {perimeter:.2f} metres")
