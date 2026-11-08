# Program purpose: Calculate weekly student expenses (using whole nairas), 
# compare them against a user-defined weekly budget, and report the financial status.

try:
    student_name = input("Enter student name: ")
    daily_transport = int(input("Enter daily transport cost (Naira): "))
    daily_feeding = int(input("Enter daily feeding cost (Naira): "))
    days_on_campus = int(input("Enter number of days on campus: "))
    other_expenses = int(input("Enter other expenses for the week (Naira): "))
    weekly_budget = int(input("Enter weekly budget (Naira): "))
except ValueError:
    print("\nError: Please enter valid whole numbers for costs, days, and budget.")
    exit()

# Validation: Reject negative values for any expense, days, or budget
if daily_transport < 0 or daily_feeding < 0 or days_on_campus < 0 or other_expenses < 0 or weekly_budget < 0:
    print("\nError: Negative values are not allowed for costs, days, or budget. Program terminated.")
else:
    # Calculations
    transport_total = daily_transport * days_on_campus
    feeding_total = daily_feeding * days_on_campus
    weekly_total = transport_total + feeding_total + other_expenses

    # Display results summary
    print("\n" + "=" * 45)
    print(f" WEEKLY BUDGET ANALYSIS: {student_name.upper()} ")
    print("=" * 45)
    print(f"Transport Total ({days_on_campus} days): ₦{transport_total}")
    print(f"Feeding Total ({days_on_campus} days):   ₦{feeding_total}")
    print(f"Other Weekly Expenses:          ₦{other_expenses}")
    print("-" * 45)
    print(f"TOTAL WEEKLY EXPENSES:          ₦{weekly_total}")
    print(f"WEEKLY BUDGET:                  ₦{weekly_budget}")
    print("-" * 45)

    # Budget comparison logic
    if weekly_total < weekly_budget:
        remaining = weekly_budget - weekly_total
        print("Status: Within budget")
        print(f"Amount remaining:               ₦{remaining}")
    elif weekly_total == weekly_budget:
        print("Status: Exactly on budget")
    else:
        exceeded = weekly_total - weekly_budget
        print("Status: Over budget")
        print(f"Amount exceeded:                ₦{exceeded}")
    print("=" * 45)
