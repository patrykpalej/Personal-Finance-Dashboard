def format_number(number):
    return f'{number:,.2f}'.replace(',', ' ') if number >= 1e4 else f'{number:.2f}'
