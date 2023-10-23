from utl.plots.lineplot import make_lineplot
from utl.db import select_data_from_time_range_for_given_table as get_data


def meta_cats(start_date, end_date, _):
    spendings_raw = get_data("home_spendings", start_date, end_date)
    spendings = spendings_raw.groupby(["metacategory", "date"]).sum(numeric_only=True)["value"]

    metacategories = list(spendings.index.levels[0].unique())

    x_values_list = []
    y_values_list = []
    names_list = []
    modes_list = []
    linestyles_list = []
    x_labels = None
    x_tickvals = None
    ylims = None

    for meta in metacategories:
        x_values_list.append(list(spendings[meta].index))
        y_values_list.append(list(spendings[meta].values))
        names_list.append(meta)
        modes_list.append("lines+markers")
        linestyles_list.append("solid")

    return make_lineplot(x_values_list, y_values_list, names_list, modes_list, linestyles_list,
                         x_labels, x_tickvals, ylims)
