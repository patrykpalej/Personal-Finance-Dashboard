from utl.plots.make_lineplot import lineplot
from utl.db import select_data_from_time_range_for_given_table as get_data


def mean_spend(start_date, end_date, _):
    spendings_raw = get_data("HOME_SPENDINGS", start_date, end_date)
    spendings = spendings_raw.groupby("DATE").sum()["VALUE"]

    moving_avg = []
    total_avg = []
    ma_coefficient = 6
    for i in range(len(spendings)):
        moving_avg.append(spendings.iloc[i-ma_coefficient+1:i+1].mean())
        total_avg.append(spendings.iloc[:i+1].mean())

    x_values_list = [spendings.index, spendings.index]
    y_values_list = [moving_avg, total_avg]
    names_list = ["Średnia krocząca (6m)", "Dotychczasowa średnia"]
    modes_list = ["lines+markers", "lines+markers"]
    linestyles_list = ["solid", "solid"]
    x_labels = None
    x_tickvals = None
    ylims = None

    return lineplot(x_values_list, y_values_list, names_list, modes_list, linestyles_list,
                    x_labels, x_tickvals, ylims)
