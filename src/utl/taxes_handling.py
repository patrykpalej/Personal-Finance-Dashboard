from config import jdg_companies


def subtract_taxes_from_earnings(earnings, taxes):
    """
    Args: df of earnings grouped by date and source, df of taxes (PIT, ZUS, VAT)
    Returns: df of earnings with taxes subtracted
    """
    earnings_minus_taxes = earnings.copy()

    for date_ in taxes.index:
        try:
            monthly_earnings = earnings[date_]
        except KeyError:
            continue

        taxed_earnings = dict()
        for source, value in monthly_earnings.items():
            if source in jdg_companies:
                taxed_earnings[source] = value

        if taxed_earnings:
            tax_info = taxes[taxes.index == date_][["pit", "zus", "vat"]]
            total_tax_per_month = float(tax_info["pit"] + tax_info["zus"] - tax_info["vat"])

            for source, earning in taxed_earnings.items():
                tax_per_source = total_tax_per_month * earning / (sum(taxed_earnings.values()))
                earnings_minus_taxes[date_][source] = earning - tax_per_source

    return earnings_minus_taxes
