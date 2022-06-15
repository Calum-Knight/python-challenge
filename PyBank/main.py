import csv
import os

months = []
ProfLoss = 0
Increase = 0
Decrease = 0

csvpath = os.path.join("Resources" ,"budget_data.csv")

with open(csvpath, encoding='utf') as csvfile:

    for row in csvfile:
        months.append(row[0])
        ProfLoss += row[1]
        if row[1] > Increase:
            Increase = row[1]
        if row[1] < decrease:
            Decrease = row[1]

print(f'Total Months: {len(months[])} \n Total: {ProfLoss} \n Average Change: {Average}')
print(f'Greatest Increase in Profits: {month:amount}')


#Total Number of Months in Data
#Net Total P&L over entire period
#Average change in profits
#Greatest Increase - Period and amount
#Greatest Decrease - Period and amount

#Print to terminal and create txt file with results