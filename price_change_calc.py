#this calculator will calculate the change in a stocks price

import pandas as pd

df = pd.read_csv("HistoricalData_1762773505397.csv")

df.rename(columns={"Close/Last": "Close"}, inplace=True)
#df["Difference"] = df["Close"] - df["Open"]

differences = []
movements = []

for index, row in df.iterrows():
    diff = row["Close"] - row["Open"]
    differences.append(diff)
    
    if diff > 0:
        movements.append("Rise")
    elif diff < 0:
        movements.append("Fall")
    else:
        movements.append("Flat")

df["Difference"] = differences
df["Movement"] = movements

print(df)

array = [0,1,2,3,4,5,6,7,8,9,]

def calc(array):
    len_array = len(array)
    for x in range (0 , (len_array-1) ):
        print( array[x+1] - array[x] )
    
#calc(array)


# order will be set as n-1