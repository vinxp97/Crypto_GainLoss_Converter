# Crypto_GainLoss_Converter
I used ChatGPT to help me create a python script that would convert gain/loss statements from a broker called Domain Money into the Koinly universal format. This was necessary as the crypto trades were fulfilled off-chain and could not be auto-imported into Koinly's crypto tax software. The script assumes all transactions are in USD and that there are no transaction fees, which may mean there was a spread for the trades that is not trackable. If the broker charges fees or if transactions occur in other currencies, the script would need to be updated.

1. Date Conversion: The script parses the 'Date Acquired' and 'Date Sold or Disposed' columns from the original dataframe, which are in ISO 8601 format. These timestamps are first converted to datetime objects, then localized to UTC timezone using the pytz library. Subsequently, they are converted to the Eastern Time Zone (ET) and then formatted into strings in the form 'YYYY-MM-DD HH:MM TZ'. These strings are stored in the 'Koinly Date' column of the new dataframe.

2. Transaction Splitting: The script creates two rows in the new dataframe for each row in the original dataframe. The first row corresponds to the 'Buy' transaction and the second row corresponds to the 'Sell' transaction. The 'Side' column of the new dataframe indicates whether the transaction is a 'Buy' or 'Sell'.

3. Column Renaming and Reordering: The script creates a new dataframe with columns corresponding to the Koinly format. The 'Property Quantity' column from the original dataframe is copied to the 'Amount' column of the new dataframe, the 'Property Symbol' column is combined with 'USD' to form the 'Pair' column, and the 'Cost Basis (USD)' and 'Proceeds (USD)' columns are renamed to 'Total' for the 'Buy' and 'Sell' transactions respectively.

4. New Columns: The script adds the columns 'Fee Amount', 'Fee Currency', 'Order ID', and 'Trade ID' to the new dataframe. 'Fee Amount' and 'Fee Currency' are filled with 0 and 'USD' respectively, while 'Order ID' and 'Trade ID' are left empty.

5. File Writing: Finally, the script writes the newly created dataframe to a CSV file.
