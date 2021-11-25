import pandas as pd
from config import db_credentials
from dbutl.make_connection import make_connection


def return_list_of_years_in_db():
    """
    Selects all spendings from db and returns a structure with all unique years
    """
    conn = make_connection(db_credentials)
    select_query = 'SELECT "DATE" FROM "HOME_SPENDINGS" ORDER BY "DATE"'
    df = pd.read_sql(select_query, conn)
    conn.close()

    unq_years = list(set([item.year for item in df["DATE"].unique()]))
    return [{"label": str(year), "value": year} for year in unq_years]


def return_list_of_months_for_given_year(year):
    """
    Return all months for a given year
    """
    conn = make_connection(db_credentials)

    select_query = f'''SELECT DISTINCT(EXTRACT(month from "DATE")) AS date FROM "HOME_SPENDINGS"
                       WHERE EXTRACT(year FROM "DATE") = {year}'''

    unq_months = [int(x) for x in pd.read_sql(select_query, conn)["date"]]
    conn.close()

    return [{"label": str(month), "value": month} for month in unq_months]
