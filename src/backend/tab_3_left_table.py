from dash import html
from utl.db import select_data_from_time_range_for_given_table as get_data


def prepare_h1(title):
    return html.Tr([html.Td([title], colSpan=3, style={"text-align": "center"})],
                   style={"height": "40px", "background-color": "#6f98ed", "width": "30vw"})


def prepare_h2():
    return html.Tr([html.Td(["Wydatek"],
                            style={"background-color": "#bcc5f7", "text-align": "center"}),
                    html.Td(["Kwota [PLN]"],
                            style={"background-color": "#bcc5f7", "text-align": "center"}),
                    html.Td(["Kategoria"],
                            style={"background-color": "#bcc5f7", "text-align": "center"})
                    ])


def prepare_row(expense, value, category):
    return html.Tr([html.Td([expense], style={"border-bottom": "1px solid black"}),
                    html.Td([value], style={"border-bottom": "1px solid black"}),
                    html.Td([category], style={"border-bottom": "1px solid black"})])


month_dict = {1: "Styczeń", 2: "Luty", 3: "Marzec", 4: "Kwiecień", 5: "Maj", 6: "Czerwiec",
              7: "Lipiec", 8: "Sierpień", 9: "Wrzesień", 10: "Październik", 11: "Listopad",
              12: "Grudzień"}


def fill_left_table(categories, start_date, end_date):
    categories_filter = f''' "CATEGORY" in ({','.join(categories)})'''
    spendings = get_data("HOME_SPENDINGS", start_date, end_date, where=categories_filter)

    unique_dates = sorted(spendings["DATE"].unique())
    monthly_sums = dict(zip(unique_dates, [sum(spendings[spendings["DATE"] == date_]["VALUE"])
                                           for date_ in unique_dates]))

    table_data = dict()
    for date_ in unique_dates:
        single_month_spendings = spendings[spendings["DATE"] == date_]

        key = f"{month_dict[date_.month]} {date_.year} - {round(monthly_sums[date_], 2)} zł"
        table_data[key] = [(row["DESCRIPTION"], row["VALUE"], row["CATEGORY"])
                           for i, row in single_month_spendings.iterrows()]

    table_body = []
    for month_title, spendings_list in table_data.items():
        table_body.append(prepare_h1(month_title))
        table_body.append(prepare_h2())
        for single_expense in spendings_list:
            table_body.append(prepare_row(*single_expense))

    return (html.Table(table_body, style={"width": "25vw"}),
            f"Suma całkowita: {round(sum(spendings['VALUE']), 2)} zł")
