import psycopg2
import pandas as pd
from config import db_credentials
from sqlalchemy import create_engine


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


def make_engine(credentials: dict):
    """
    Creates sqlalchemy.engine.base.Engine object based on credentials dictionary
    Parameters
    ----------
    credentials: dict
    """
    try:
        conn_str = (f"postgresql://{credentials['user']}:{credentials['password']}"
                    f"@{credentials['host']}:{credentials['port']}/{credentials['dbname']}")
        engine = create_engine(conn_str)
        return engine
    except Exception as e:
        print(e)
        return None


def return_list_of_unique_years_in_db():
    """
    Selects all spendings from db and uses it to return a list of all unique years
    """
    conn = make_connection(db_credentials)
    select_query = '''SELECT DISTINCT(EXTRACT(year from date)) AS unq_year
                      FROM home_spendings'''
    df = pd.read_sql(select_query, conn)
    conn.close()

    unique_years_in_db = sorted([int(year) for year in df["unq_year"]])
    return unique_years_in_db


def return_list_of_months_for_given_year(year):
    """
    Return all months for a given year
    """
    if not year:
        return []

    conn = make_connection(db_credentials)

    select_query = f'''SELECT DISTINCT(EXTRACT(month from date)) AS date FROM home_spendings
                       WHERE EXTRACT(year FROM date) = {year}'''

    unq_months = [int(x) for x in pd.read_sql(select_query, conn)["date"]]
    conn.close()

    return unq_months


def select_data_from_time_range_for_given_table(table_name, start_date, end_date, where=None):
    select_query = f'''SELECT * FROM {table_name} WHERE date >= 
    '{start_date}' AND date <= '{end_date}' '''
    if where is not None:
        select_query += f"AND {where}"

    conn = make_connection(db_credentials)
    results = pd.read_sql(select_query, conn)
    conn.close()

    return results
