""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    # Parse the date string into separate year, month, day, hour, minute, and second components
    year, month, day, hour, minute, second = map(
        int, datestr.replace("T", "-").replace(":", "-").split("-"))

    # Create and return a new datetime object
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2022-12-01T01:02:03'
    print(f'{logstamp_to_datetime(test_date)=}')
