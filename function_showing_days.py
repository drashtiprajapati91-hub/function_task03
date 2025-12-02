from datetime import datetime, timedelta

def get_tue_and_fri(year, month):
    tue = []
    fri = []

    # Start from the first day of the month
    date = datetime(year, month, 1)

    # Loop through all days of the month
    while date.month == month:
        if date.weekday() == 1:
            tue.append(date.strftime("%Y-%m-%d"))
        if date.weekday() == 4:
            fri.append(date.strftime("%Y-%m-%d"))
        
        date += timedelta(days=1)

    return tue, fri

# Get user input
year = int(input("Enter year (e.g., 2025): "))
month = int(input("Enter month (1-12): "))

# Get dates
tue, fri = get_tue_and_fri(year, month)

# Print results
print("\n tuesdays:")
for d in tue:
    print(d)

print("\n fridays:")
for d in fri:
    print(d)
