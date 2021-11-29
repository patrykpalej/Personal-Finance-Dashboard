from utl.general import format_number
from utl.db import select_data_from_time_range_for_given_table as get_data


def calculate_balance(accounts_names, amounts):
    incomes_df = get_data("HOME_INCOMES", '2000-01-01', '2099-12-31')
    spendings_df = get_data("HOME_SPENDINGS", '2000-01-01', '2099-12-31')
    taxes_df = get_data("HOME_TAXES", '2000-01-01', '2099-12-31')

    sum_of_savings = sum([float(x) for x in amounts if x is not None])

    income_gross = incomes_df["VALUE"].sum() + taxes_df["VAT"].sum()
    outcome_gross = (spendings_df["VALUE"].sum() + sum_of_savings + taxes_df["PIT"].sum() +
                     taxes_df["ZUS"].sum())

    balance = outcome_gross - income_gross

    table_data = [{"Suma przychodów": format_number(incomes_df["VALUE"].sum()),
                   "Suma wydatków": format_number(spendings_df["VALUE"].sum()),
                   "Suma oszczędności": format_number(sum_of_savings),
                   "Bilans": format_number(balance)}]

    return table_data, accounts_names
