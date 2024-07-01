# df creator using predictits csv downloads that are available
import pandas as pd 

# to get the csv data
import requests

def data(market, time):
    #24h,7d,30d, 90d
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    url = 'https://www.predictit.org/Resource/DownloadMarketChartData?marketid='+str(market)+'&timespan='+str(time)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
      # Download successful, proceed with data processing
      with open('market_data.csv', 'wb') as f:
        f.write(response.content)
    else:
        print(f"Error downloading data: {response.status_code}")

    df = pd.read_csv('market_data.csv')

    # the following code is to clean the data:

    # filter out unnecessary columns
    df = df[['ContractName', 'Date', 'CloseSharePrice']]

    # convert "ContractName" values to column names
    df = df.pivot(index='Date', columns='ContractName', values='CloseSharePrice')

    # remove dollar signs from values
    df = df.replace('[$,]', '', regex=True).astype(float)

    # remove "ContractName" column
    df.columns.name = None

    # Convert Date to datetime in date format
    df.index = pd.to_datetime(df.index)

    # sort by date, descending
    df = df.sort_index(ascending=False)

    return df
    
def market_name(market):
    # this may not be the best way to do it, but it worked pretty well for me 
    df = pd.read_json('https://www.predictit.org/api/marketdata/markets/'+str(market))
    # sets the market to a string and returns it. 
    text = str(df['name'][0])
    return text
