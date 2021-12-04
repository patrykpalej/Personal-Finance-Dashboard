from dash import html

from config import month_dict


def prepare_dates_range_to_display(start_date, end_date):
    return f"Zakres dat: {start_date.month}.{start_date.year} - {end_date.month}.{end_date.year}"


def prepare_html_table_h1(title):
    return html.Tr([html.Td([title], colSpan=3, style={"text-align": "center"})],
                   style={"height": "40px", "background-color": "#6f98ed", "width": "30vw"})


def prepare_html_table_h2():
    return html.Tr([html.Td(["Wydatek"],
                            style={"background-color": "#bcc5f7", "text-align": "center",
                                   "width": "12vw"}),
                    html.Td(["Kwota [PLN]"],
                            style={"background-color": "#bcc5f7", "text-align": "center",
                                   "width": "6vw"}),
                    html.Td(["Kategoria"],
                            style={"background-color": "#bcc5f7", "text-align": "center",
                                   "width": "12vw"})])


def prepare_html_table_row(expense, value, category):
    return html.Tr([html.Td([expense], style={"border-bottom": "1px solid black"}),
                    html.Td([value], style={"border-bottom": "1px solid black"}),
                    html.Td([category], style={"border-bottom": "1px solid black"})])


def make_html_table(df):
    """
    Used in tab_3 (left collation table) and tab_4 (spendings finder) to transform
    pandas dataframe to a html table grouped by date
    """
    unique_dates = sorted(df["DATE"].unique())
    monthly_sums = dict(zip(unique_dates, [sum(df[df["DATE"] == date_]["VALUE"])
                                           for date_ in unique_dates]))

    table_data = dict()
    for date_ in unique_dates:
        single_month_spendings = df[df["DATE"] == date_]

        key = f"{month_dict[date_.month]} {date_.year} - {round(monthly_sums[date_], 2)} zł"
        table_data[key] = [(row["DESCRIPTION"], row["VALUE"], row["CATEGORY"])
                           for i, row in single_month_spendings.iterrows()]

    table_body = []
    for month_title, spendings_list in table_data.items():
        table_body.append(prepare_html_table_h1(month_title))
        table_body.append(prepare_html_table_h2())
        for single_expense in spendings_list:
            table_body.append(prepare_html_table_row(*single_expense))

    return table_body
