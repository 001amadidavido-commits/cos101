# Convert a whole number of minutes into hours and remaining minutes.

total_minutes = int(input("Enter the total number of minutes: "))

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print("Hours:", hours)
print("Remaining minutes:", remaining_minutes)
