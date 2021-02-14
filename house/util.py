from datetime import datetime
from dateutil.relativedelta import relativedelta


def yearsago(years, from_date=None):
    if from_date is None:
        from_date = datetime.now()
    return from_date - relativedelta(years=years)


def num_years(begin, end=None):
    if end is None:
        end = datetime.now()
    num_years = int((end - begin).days / 365.2425)
    if begin > yearsago(num_years, end):
        return num_years - 1
    else:
        return num_years
