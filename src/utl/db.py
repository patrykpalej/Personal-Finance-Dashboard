import psycopg2
import pandas as pd
from config import db_credentials


def make_connection(credentials: dict):
    """
    Creates psycopg2.Connection object based on credentials dictionary
    Parameters
    ----------
    credentials: dict
    """
    try:
        conn = psycopg2.connect(**credentials)
        return conn
    except Exception as e:
        print(e)
        return None


def return_list_of_unique_years_in_db():
    """
    Selects all spendings from db and uses it to return a list of all unique years
    """
    conn = make_connection(db_credentials)
    select_query = '''SELECT DISTINCT(EXTRACT(year from "DATE")) AS "UNQ_YEAR"
                      FROM "HOME_SPENDINGS"'''
    df = pd.read_sql(select_query, conn)
    conn.close()

    unique_years_in_db = sorted([int(year) for year in df["UNQ_YEAR"]])
    return unique_years_in_db


def return_list_of_months_for_given_year(year):
    """
    Return all months for a given year
    """
    if not year:
        return []

    conn = make_connection(db_credentials)

    select_query = f'''SELECT DISTINCT(EXTRACT(month from "DATE")) AS date FROM "HOME_SPENDINGS"
                       WHERE EXTRACT(year FROM "DATE") = {year}'''

    unq_months = [int(x) for x in pd.read_sql(select_query, conn)["date"]]
    conn.close()

    return unq_months


def select_data_from_time_range_for_given_table(table_name, start_date, end_date):
    select_query = f'''SELECT * FROM "{table_name}"
                       WHERE "DATE" >= '{start_date}' AND "DATE" <= '{end_date}' '''
    conn = make_connection(db_credentials)
    results = pd.read_sql(select_query, conn)
    conn.close()

    return results
