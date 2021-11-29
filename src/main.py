from app import app

import callbacks.tab_1_set_time_range
import callbacks.tab_1_make_charts
import callbacks.tab_2_stats_table
import callbacks.tab_3_collations


if __name__ == '__main__':
    app.run_server(debug=True, port=3456, host='0.0.0.0')
