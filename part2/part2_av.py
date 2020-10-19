"""
Requirements: 
    1. Retrieve the historical time series data from the API. For this, use the endpoint for the "Daily Digital & Crypto Currencies", specifying as symbol ‘BTC’ and as market ‘USD’
    2. Data Transformation
        Compute the average CLOSE price of each week
        Compute a 3-day and 7-day rolling CLOSE PRICE average and report/visualise the results. 
"""


import requests
import alpha_vantage
import json 
import pandas as pd
import os 
from datetime import timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

class alpha_vantage_time_series:
    def __init__(self):
        self.url_api = "https://www.alphavantage.co/query"
        self.api_key = os.getenv('alpha_vantage_api_key')

    def fetch_api(self, function, symbol, market): 
        api_parameters = { "function": function, 
                "symbol": symbol, 
                "market": market,  
                "apikey": self.api_key } 
        response = requests.get(self.url_api, api_parameters) 
        data_json = response.json()

        # Convert to dataframe 
        data = pd.DataFrame([], columns = ["date", "close_price_usd"])

        for date_key in data_json["Time Series (Digital Currency Daily)"].keys():
            daily_stats = data_json["Time Series (Digital Currency Daily)"][date_key]
            data = data.append({"date": date_key, "close_price_usd": float(daily_stats["4a. close (USD)"])}, ignore_index = True)

        # Truncate date column by week, start from Monday 
        data["date"] = pd.to_datetime(data["date"])
        # Convert date column to day of week
        data['dow'] = data['date'].apply(lambda x: x.weekday())
        data['week'] = data.apply(lambda x: x["date"] - timedelta(days=x["dow"]), axis=1)
        self.data = data
    
    def weekly_report(self):
        # Compute the average CLOSE price of each week
        data_agg_week = self.data.groupby(["week"])["week","close_price_usd"].mean().sort_values("week")
        
        # Save report as CSV
        data_agg_week.to_csv("part2/average_btc_closing_price_weekly_report.csv")

        # Visualise average CLOSE price of each week 
        plt.style.use('fivethirtyeight')
        plt.plot_date(data_agg_week.index, data_agg_week["close_price_usd"], linestyle='solid')
        plt.gcf().autofmt_xdate()

        plt.title('BTC Average Weekly Closing Price')
        plt.ylabel('Closing Price')
        fig = plt.gcf()
        fig.set_size_inches(18.5, 10.5)
        plt.savefig("part2/average_btc_closing_price_weekly_plot.png")

    def moving_average(self, rolling_window_1, rolling_window_2):
        # Compute rolling windows 
        data_rolling_window_1 = self.data["close_price_usd"].rolling(window = rolling_window_1).mean()
        data_rolling_window_2 = self.data["close_price_usd"].rolling(window = rolling_window_2).mean()

        # Convert to dataframe and save report as CSV
        data_rolling_window_1_df = pd.DataFrame(data_rolling_window_1)
        data_rolling_window_1_df.rename(columns= {"close_price_usd": "rolling_{}_day_average_closing_price_usd".format(rolling_window_1)}, inplace = True)

        data_rolling_window_2_df = pd.DataFrame(data_rolling_window_2)
        data_rolling_window_2_df.rename(columns= {"close_price_usd": "rolling_{}_day_average_closing_price_usd".format(rolling_window_2)}, inplace = True)

        data_rolling_average = pd.concat([self.data, data_rolling_window_1_df, data_rolling_window_2_df], axis = 1)
        data_rolling_average.to_csv("part2/rolling_average_btc_closing_price_weekly_report.csv")

        plt.plot(self.data["date"], self.data["close_price_usd"], label="Daily Closing Price")
        plt.plot(self.data["date"], data_rolling_window_1, label="Rolling {} day Average".format(rolling_window_1), color='blue')
        plt.plot(self.data["date"], data_rolling_window_2, label="Rolling {} day Average".format(rolling_window_2), color='red')
        plt.legend(loc='upper left')
        plt.title('BTC Closing Price')
        plt.ylabel('Closing Price')
        fig = plt.gcf()
        fig.set_size_inches(18.5, 10.5)
        plt.savefig("part2/rolling_average_btc_closing_price_weekly_plot.png")
        




