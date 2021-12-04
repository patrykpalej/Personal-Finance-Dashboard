import os
import json
from dotenv import load_dotenv


load_dotenv()

# CREDENTIALS
db_environment_variables = ["DBNAME", "DBUSER", "PASSWORD", "HOST", "PORT"]
envvar_dictkeys_dict = {"DBNAME": "dbname", "DBUSER": "user", "PASSWORD": "password",
                        "HOST": "host", "PORT": "port"}
db_credentials = dict()
for variable in db_environment_variables:
    db_credentials[envvar_dictkeys_dict[variable]] = os.getenv(variable)

dash_auth_password = os.getenv('DASH_AUTH_PASSWORD')


# CONSTANTS
BALANCE_N_INPUTS = 12


# JSONS
with open("config/bank_accounts.json", "r") as f:
    bank_accounts = json.load(f)

with open("config/jdg_companies.json", "r") as f:
    jdg_companies = json.load(f)

with open("config/long_chart_names.json", "r") as f:
    long_chart_names = json.load(f)

with open("config/short_chart_names.json", "r") as f:
    short_chart_names = json.load(f)

with open("config/tax_info.json", "r") as f:
    tax_info = json.load(f)

with open("config/spendings_metacategories.json", "r") as f:
    metacategories_dict = json.load(f)


# DB TABLES AD EXCEL DATA
with open("config/db_tables/home_earnings.json", "r") as f:
    home_earnings_config = json.load(f)

with open("config/db_tables/home_incomes.json", "r") as f:
    home_incomes_config = json.load(f)

with open("config/db_tables/home_spendings.json", "r") as f:
    home_spendings_config = json.load(f)

with open("config/db_tables/home_longterm.json", "r") as f:
    home_longterm_config = json.load(f)

with open("config/db_tables/home_taxes.json", "r") as f:
    home_taxes_config = json.load(f)

with open("config/path_to_monthly_data.json", "r") as f:
    path_to_monthly_data = json.load(f)[0]

# OTHER
month_dict = {1: "Styczeń", 2: "Luty", 3: "Marzec", 4: "Kwiecień", 5: "Maj", 6: "Czerwiec",
              7: "Lipiec", 8: "Sierpień", 9: "Wrzesień", 10: "Październik", 11: "Listopad",
              12: "Grudzień"}
