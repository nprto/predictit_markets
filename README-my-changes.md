# predictit_markets
Simple Python code that helps to retrieve predictit market data. 

# data
Given a number, returns a [Pandas](https://pandas.pydata.org/docs/) dataframe of the market data. It attempts to grab the last 90 days, but can be changed to 24h,7d, or 30d as well. Constructor defaults to '90d', but can take the other dates as an argument. 

The data function returned 403 errors when I ran it, perhaps because PredictIt changed its policy since tuttlepower created his code. I added a header and replaced pd.read_csv(url) with requests.get(url, headers=headers).

Additionally, I added lines to the 'data' function to clean the data and make it more presentable for my own purposes.

Finally, I included a juypyter notebook file with the same code, in addition to the .py file. 

`df = data(7456)`

`print(df.head())`

![alt text](https://github.com/tuttlepower/predictit_markets/blob/master/images/output_example.PNG "Output Example")

# market_name

`print(market_name(7456))`

Returns the name of the market as a string. 

'Who will win the 2024 US presidential election?'

That's all there is to it. Predictit's API is in XML format, which I thought was a pain, and they have download buttons for every market. I found [this](https://gist.github.com/kiernann/bf5ba187a5070ecb6cfe34db76860c45) and it helped me understand the urls that are used to download the market CSV's so I recreated it for Python. I didn't see anything else like this posted, and I figured it may help someone else down the line. Was considering putting this as a package, but it doesn't seem like it would be worth it. 
