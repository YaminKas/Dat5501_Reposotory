#this calculator will calculate the change in price
array = [0,1,2,3,4,5,6,7,8,9,]

def calc(array):
    len_array = len(array)
    for x in range (0 , (len_array-1) ):
        print( array[x+1] - array[x] )
    
#calc(array)


# order will be set as n-1


# the code below this take in the price data of EURUSD and then retunr the price differnce for 11/24 - 11/25
# it return the difference to 3 decimal places and whether the movement was a rise or fall in price.

import pandas as pd

df = pd.read_csv("HistoricalData_1762773505397.csv")

df.rename(columns={"Close/Last": "Close"}, inplace=True)
#df["Difference"] = df["Close"] - df["Open"]

differences = []
movements = []

for index, row in df.iterrows():
    difference_in_price = (row["Close"] - row["Open"])
    differences.append(round(difference_in_price,3))
    
    if difference_in_price > 0:
        movements.append("Rise in price")
    elif difference_in_price < 0:
        movements.append("Fall in price")
    else:
        movements.append("No change in price")

df["Difference"] = differences
df["Movement"] = movements


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df)
