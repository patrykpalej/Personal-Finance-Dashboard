import pandas as pd
from config import db_credentials
from dbutl.make_connection import make_connection


def return_list_of_years_in_db():
    """
    Selects all spendings from db and returns a structure with all unique years
    """
    conn = make_connection(db_credentials)
    select_query = '''SELECT "DATE" FROM "HOME_SPENDINGS" ORDER BY "DATE"'''
    df = pd.read_sql(select_query, conn)
    unq_years = list(set([item.year for item in df["DATE"].unique()]))
    return [{"label": str(year), "value": str(year)} for year in unq_years]
