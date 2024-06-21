from datetime import datetime


class DateHandler:

    def __init__(self) -> None:
        pass

    # factory method
    @classmethod
    def format_date(cls, date):
        return date.strftime("%d/%m/%Y")

    @classmethod
    def get_days_between(date1, date2):
        return (date1 - date2).days


# test driver
start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)
print("Start:", DateHandler.format_date(start_date))
print("End:", DateHandler.format_date(end_date))
print("Days between:", DateHandler.get_days_between(start_date, end_date))
