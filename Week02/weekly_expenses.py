# student_budget.py
# Program purpose: Calculate weekly student expenses including transport, feeding, and miscellaneous costs.

# 1. Collect user inputs
student_name = input("Enter student name: ")
daily_transport = float(input("Enter daily transport cost: "))
daily_feeding = float(input("Enter daily feeding cost: "))
days_on_campus = int(input("Enter number of days on campus: "))
other_expenses = float(input("Enter other expenses for the week: "))

# 2. Perform calculations
transport_total = daily_transport * days_on_campus
feeding_total = daily_feeding * days_on_campus
weekly_total = transport_total + feeding_total + other_expenses

# 3. Display the results
print("\n" + "=" * 40)
print(f" WEEKLY EXPENSE SUMMARY FOR: {student_name.upper()} ")
print("=" * 40)
print(f"Transport Total ({days_on_campus} days): ${transport_total:.2f}")
print(f"Feeding Total ({days_on_campus} days):   ${feeding_total:.2f}")
print(f"Other Weekly Expenses:          ${other_expenses:.2f}")
print("-" * 40)
print(f"TOTAL WEEKLY EXPENSES:          ${weekly_total:.2f}")
print("=" * 40)
