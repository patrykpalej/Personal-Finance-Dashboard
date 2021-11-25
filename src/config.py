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
