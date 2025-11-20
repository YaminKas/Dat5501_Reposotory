import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load CSV

df = pd.read_csv('bitcoin.csv')

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Sort by date (oldest first)
df = df.sort_values('Date')


# Plot the data
plt.figure(figsize=(14,7))

# Plot Close/Last
plt.plot(df['Date'], df['Close/Last'], marker='o', linestyle='-', color='blue', label='Close PRICE')



plt.title("Bitcoin Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.legend()

# Auto-format date labels
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d %y'))
plt.gcf().autofmt_xdate()

plt.tight_layout()

# Save figure
plt.savefig("bitcoin_plot.png", dpi=150)
plt.show()