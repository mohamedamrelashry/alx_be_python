from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now().date()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)
def calculate_future_date(daysToAdd):
    future_date = datetime.now() + timedelta(days=daysToAdd)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

display_current_datetime()
daysToAdd = input("Enter the number of days to add to the current date:")
calculate_future_date(daysToAdd)
