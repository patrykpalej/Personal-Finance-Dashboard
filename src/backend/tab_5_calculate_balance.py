from utl.general import format_number
from utl.db import select_data_from_time_range_for_given_table as get_data


def calculate_balance(accounts_names, amounts):
    incomes_df = get_data("home_incomes", '2000-01-01', '2099-12-31')
    spendings_df = get_data("home_spendings", '2000-01-01', '2099-12-31')
    taxes_df = get_data("home_taxes", '2000-01-01', '2099-12-31')

    sum_of_savings = sum([float(x) for x in amounts if x is not None])

    income_gross = incomes_df["value"].sum() + taxes_df["vat"].sum()
    outcome_gross = (spendings_df["value"].sum() + sum_of_savings + taxes_df["pit"].sum() +
                     taxes_df["zus"].sum())

    balance = outcome_gross - income_gross

    table_data = [{"Suma przychodów": format_number(incomes_df["value"].sum()),
                   "Suma wydatków": format_number(spendings_df["value"].sum()),
                   "Suma oszczędności": format_number(sum_of_savings),
                   "Bilans": format_number(balance)}]

    return table_data, accounts_names
