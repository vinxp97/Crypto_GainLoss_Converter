import pandas as pd
from datetime import datetime
import pytz

# read in the source CSV file
df = pd.read_csv('/Users/johndoe/Documents/Coding/Python/statements/Original.csv')

# create a new dataframe for the converted data
converted_df = pd.DataFrame(columns=['Koinly Date', 'Pair', 'Side', 'Amount', 'Total', 'Fee Amount', 'Fee Currency', 'Order ID', 'Trade ID'])

# loop through each row in the source data
for i, row in df.iterrows():
    # parse the timestamp strings
    acquired_date = datetime.strptime(row['Date Acquired'][:-5], '%Y-%m-%dT%H:%M:%S')
    sold_date = datetime.strptime(row['Date Sold or Disposed'][:-5], '%Y-%m-%dT%H:%M:%S')
    # add UTC timezone information
    acquired_date = pytz.utc.localize(acquired_date)
    sold_date = pytz.utc.localize(sold_date)
    # create a new row for the buy transaction
    buy_row = {
        'Koinly Date': acquired_date.astimezone(pytz.timezone('US/Eastern')).strftime('%Y-%m-%d %H:%M %Z'),
        'Pair': f"{row['Property Symbol']}-USD",
        'Side': 'Buy',
        'Amount': row['Property Quantity'],
        'Total': row['Cost Basis (USD)'],
        'Fee Amount': 0,
        'Fee Currency': 'USD',
        'Order ID': '',
        'Trade ID': ''
    }
    # create a new row for the sell transaction
    sell_row = {
        'Koinly Date': sold_date.astimezone(pytz.timezone('US/Eastern')).strftime('%Y-%m-%d %H:%M %Z'),
        'Pair': f"{row['Property Symbol']}-USD",
        'Side': 'Sell',
        'Amount': row['Property Quantity'],
        'Total': row['Proceeds (USD)'],
        'Fee Amount': 0,
        'Fee Currency': 'USD',
        'Order ID': '',
        'Trade ID': ''
    }
    # add both rows to the converted dataframe
    converted_df = converted_df.append(buy_row, ignore_index=True)
    converted_df = converted_df.append(sell_row, ignore_index=True)

# write the converted data to a CSV file
converted_df.to_csv('/Users/johndoe/Documents/Coding/Python/statements/Revised.csv', index=False)

