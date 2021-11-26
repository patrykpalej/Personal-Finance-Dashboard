from app import app

from callbacks.set_time_range import (
    set_start_years_list, set_start_months_list_based_on_start_year,
    set_end_years_list_based_on_start_date, set_end_months_list_based_on_start_date_and_end_year)


if __name__ == '__main__':
    app.run_server(debug=True, port=3456, host='0.0.0.0')
