import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

profit_data=[]
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    num_rows = 0
    for row in csvreader:
        profit_data.append(row)
        num_rows += 1

num_months = num_rows -1 
print("Total Months: " +str(num_months))

total_profit_loss=0
for i in range(1,len(profit_data)):
    profit_data[i][1]=int(profit_data[i][1])
    total_profit_loss=total_profit_loss+profit_data[i][1]
print("Total net profit: " , total_profit_loss)

change=[]
for i in range(2,len(profit_data)):
    change.append(profit_data[i][1]-profit_data[i-1][1])

avg_change=sum(change)/len(change)
print("Average change: " , avg_change)

max_index=change.index(max(change))
min_index=change.index(min(change))

print("Greatest increase in profits: " , profit_data[max_index+2][0], change[max_index])
print("Greatest decrease in profits: " , profit_data[min_index+2][0], change[min_index])
