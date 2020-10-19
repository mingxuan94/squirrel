from part2_av import alpha_vantage_time_series
alpha_vantage = alpha_vantage_time_series()

#  Retrieve raw historical time series data from API
alpha_vantage.fetch_api(function = "DIGITAL_CURRENCY_DAILY", symbol = "BTC", market = "USD")

# Download weekly CSV report and visualisation 
alpha_vantage.weekly_report()

# Download rolling windows CSV reports and visualisation 
alpha_vantage.moving_average(rolling_window_1 = 3, rolling_window_2 = 7)
