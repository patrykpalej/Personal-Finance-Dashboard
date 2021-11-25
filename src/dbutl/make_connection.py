import psycopg2


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
