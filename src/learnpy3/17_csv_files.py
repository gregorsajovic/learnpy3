# Reading CSV file
path = "./data/google_stock_data.csv"
file = open(path)

for line in file:
 print(line)

lines = [line for line in open(path)]
print(lines[0])
print(lines[1])

print(lines[3].strip())

print(lines[0].strip().split(','))

dataset = [line.strip().split(',') for line in open(path)]

print(dataset[14])

import csv
from datetime import datetime
# print(dir(csv))

path = "./data/google_stock_data.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # The first line is the header
# data = [row for row in reader] # Read the remaining data

data = []
for row in reader:
 # row = [Date, Open, High, Low, Close, Volue, Adj. Close]
 date = datetime.strptime(row[0], '%m/%d/%Y')
 open_price = float(row[1]) # 'open' is a builtin function
 high = float(row[2])
 low = float(row[3])
 close = float(row[4])
 volume = int(row[5])
 adj_close = float(row[6])

 data.append([date, open_price, high, low, close, volume, adj_close])

print(header)
print(data[0])

# In finance -> Stock Return = % change in price from one day to the next
# Common time frames:
# >> Daily
# >> Weekly
# >> Monthly
# >> Annual

# Compute and store dily stock returns
returns_path = "./data/google_stock_data_with_returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data)-1):
 todays_row = data[i]
 todays_date = todays_row[0]
 todays_price = todays_row[-1]
 yesterdays_row = data[i+1]
 yesterdays_price = yesterdays_row[-1]

 daily_return = (todays_price - yesterdays_price) / yesterdays_price
 formated_date = todays_date.strftime('%m/%d/%Y')
 writer.writerow([formated_date, daily_return])

