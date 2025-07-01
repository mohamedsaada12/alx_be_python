from datetime import datetime, timedelta  # ✔️ Required import

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # ✔️ Format required
    print("Current date and time:", formatted_date)
    return formatted_date  # ✔️ Must return the formatted date

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    future_date = datetime.now() + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # ✔️ Format like YYYY-MM-DD
    print("Future date:", formatted_future_date)
    return formatted_future_date  # ✔️ Must return the future date
