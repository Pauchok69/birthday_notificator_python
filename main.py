from datetime import datetime, timedelta

test_users = [
    {"name": "Tanya", "birthday": datetime(year=1992, month=9, day=23)},
    {"name": "Kostya", "birthday": datetime(year=1992, month=3, day=8)},
    {"name": "Serhiy", "birthday": datetime(year=1992, month=3, day=8)},
    {"name": "Sasha", "birthday": datetime(year=1994, month=11, day=3)},
    {"name": "Nastya", "birthday": datetime(year=1989, month=9, day=29)},
    {"name": "Vasya", "birthday": datetime(year=1986, month=9, day=24)},
    {"name": "Pasha", "birthday": datetime(year=1986, month=9, day=27)},
    {"name": "Pasha Padlo", "birthday": datetime(year=1986, month=9, day=26)},
    {"name": "I Ego Brat", "birthday": datetime(year=1986, month=9, day=26)},
    {"name": "Nezhdanchik", "birthday": datetime(year=1986, month=10, day=1)},
    {"name": "Olia", "birthday": datetime(year=1995, month=9, day=30)}
]


def get_birthdays_per_week(users: list):
    current_day = datetime.now()

    days_interval = define_days_interval(current_day)

    new_time_line = current_day + days_interval

    user_list = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }

    for user in users:
        new_date_for_user = datetime(
            year=current_day.year,
            month=user.get('birthday').month,
            day=user.get('birthday').day
        )

        if current_day < new_date_for_user <= new_time_line:
            weekday_string = new_date_for_user.strftime("%A")

            if weekday_string in ['Saturday', 'Sunday']:
                weekday_string = 'Monday'
            user_list.get(weekday_string).append(user.get('name'))

    print_users_list(user_list)


def define_days_interval(current_day: datetime) -> timedelta:
    if current_day.weekday() == 5:
        days_interval = timedelta(days=6)
    elif current_day.weekday() == 6:
        days_interval = timedelta(days=5)
    else:
        days_interval = timedelta(days=7)

    return days_interval


def print_users_list(users_list: dict):
    for key, value in users_list.items():
        if value:
            print(f"{key}: {', '.join(value)}")


if __name__ == '__main__':
    get_birthdays_per_week(test_users)
