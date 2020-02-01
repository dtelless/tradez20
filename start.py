import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import mplfinance as mpf

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("WINN_M5_2019.csv", header=0, parse_dates=[['DATE', 'TIME']], index_col=0, sep="\t",
                   squeeze=True)

# Preview the first 5 lines of the loaded data
# data.reset_index(inplace=True)
# data['DATE_TIME'] = data['DATE_TIME'].map(mdates.date2num)

print(data.head())

mpf.plot(data)
