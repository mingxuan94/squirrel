# Analysis on the historical time series of Cryptocurrency 

## Implementation
- Using Alpha Vantage API, fetch historical daily records of BTC 
- Compute the average of Close Price for each week 
- Compute the 3 day and 7 day rolling average of Close Price 

## How to run 

### 1. Obtain API key and save it as a variable in your OS environment with variable name 'alpha_vantage_api_key' using the following command
- `launchctl setenv alpha_vantage_api_key "YOUR API KEY"`
- to check if environment variable has been set successfully, run this command `launchctl getenv variable`

### 2. Download this folder and set your working directory as `/part2` 
- [Optional] Pip install packages using the following command `pip3 install -r requirements.txt`

### 3. Run `python3 download_reports.py` in your terminal 
- Reports and plots should be automatically downloaded in the folder 

