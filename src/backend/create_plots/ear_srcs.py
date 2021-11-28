from utl.plots.lineplot import make_lineplot
from utl.taxes_handling import subtract_taxes_from_earnings
from utl.db import select_data_from_time_range_for_given_table as get_data


def ear_srcs(start_date, end_date, additional_settings):
    earnings_raw = get_data("HOME_EARNINGS", start_date, end_date)
    earnings = earnings_raw.groupby(["DATE", "SOURCE"]).sum()["VALUE"]

    if "subtract_tax" in additional_settings:
        taxes = get_data("HOME_TAXES", start_date, end_date)
        earnings = subtract_taxes_from_earnings(earnings, taxes)

    ordered_sources = earnings_raw.groupby("SOURCE").sum()["VALUE"].sort_values(ascending=False)
    threshold_percentage = 0.04
    top_sources = []
    for src, all_earnings_from_src in ordered_sources.iteritems():
        if all_earnings_from_src > threshold_percentage * sum(ordered_sources):
            top_sources.append(src)
        else:
            break
    sources_labels = top_sources + ["Inne"]

    unq_dates = sorted(list(set([idx[0] for idx in earnings.index])))
    earnings_matrix = [[0] * len(unq_dates) for _ in sources_labels]
    for d, date_ in enumerate(unq_dates):
        single_month_earnings = earnings.loc[date_]
        for src_label, value in single_month_earnings.iteritems():
            if src_label in top_sources:
                earnings_matrix[sources_labels.index(src_label)][d] += value
            else:
                earnings_matrix[sources_labels.index("Inne")][d] += value

    x_values_list = [unq_dates] * len(sources_labels)
    y_values_list = earnings_matrix
    names_list = sources_labels
    modes_list = ["lines+markers"] * len(sources_labels)
    linestyles_list = ["solid"] * len(sources_labels)

    return make_lineplot(x_values_list, y_values_list, names_list, modes_list, linestyles_list)
