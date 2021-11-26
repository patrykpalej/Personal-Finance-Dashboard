from datetime import date
from utl.db import return_list_of_unique_years_in_db, return_list_of_months_for_given_year


def generate_end_years_list_based_on_start_date(start_year_set_in_dash, start_month_set_in_dash):
    """
    Return list of end date's years based on start date
    """
    if not all([start_year_set_in_dash, start_month_set_in_dash]):
        return []

    latest_year_in_db = max(return_list_of_unique_years_in_db())
    all_possible_end_years = list(range(start_year_set_in_dash, latest_year_in_db + 1))

    return all_possible_end_years


def generate_end_months_list_based_on_start_date_and_end_year(
        start_year_set_in_dash, start_month_set_in_dash, end_year_set_in_dash):
    """
    Return list of end dates' months based on end start date and end year
    """
    if not all([start_year_set_in_dash, start_month_set_in_dash, end_year_set_in_dash]):
        return []

    all_months_for_end_year = return_list_of_months_for_given_year(end_year_set_in_dash)
    start_date_set_in_dash = date(start_year_set_in_dash, start_month_set_in_dash, 1)

    return [month for month in all_months_for_end_year
            if start_date_set_in_dash <= date(end_year_set_in_dash, month, 1)]
