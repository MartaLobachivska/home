from datetime import date, datetime


def get_birthdays_per_week(users):
    today = date.today()
    next_week = today + datetime
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] 
    birthdays = {day: [] for day in days_of_week}
    for user in users:
        name = user['name']
        birthday = user['birthday'] 
        this_year_birthday = birthday.replace(year=today.year)
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
