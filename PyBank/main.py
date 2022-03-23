# 1.    The total number of months included in the dataset
# 2.    The net total amount of "Profit/Losses" over the entire period
# 3.    The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 4.    The greatest increase in profits (date and amount) over the entire period
# 5.    The greatest decrease in profits (date and amount) over the entire period

# #Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# import os and csv modules
import os
import csv

#CSV path file
csvpath = os.path.join('Resources', 'budget_data.csv')

#List to store data
profit = []
changes = []
months = []

#variables
count = 0
total_profit = 0
profit_change = 0
initial_profit = 0

# to open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f'CSV Header: {csv_header}') - to read out the headers in the terminal 

    for row in csvreader:
        #print(row) - to check that I am able to read the csv file in terminal
        count = count + 1
        #Append list for months and profit
        months.append(row[0])
        profit.append(row[1])
        total_profit = total_profit + int(row[1])

        #calculating average change from month to month
        final_profit = int(row[1])
        monthly_change_profit = final_profit - initial_profit

        #list for monthly change profit
        changes.append(monthly_change_profit)
        profit_change = profit_change + monthly_change_profit
        initial_profit = final_profit

        # Average Change for profits
        average_change = (profit_change / count)

        #finding max and min for the profits
        greatest_increase = max(changes)
        greatest_decrease = min(changes)

        #date for greatest increase and decrease
        increase_date = months[changes.index(greatest_increase)]
        decrease_date = months[changes.index(greatest_decrease)]
    
    #Print Statements
    print("Financial Analysis")
    print("--------------------------------------------")
    print("Total Months: " + str(count))
    print("Total: $", str(total_profit))
    print("Average Change: $" + str(int(average_change)))
    print("Greatest Increase in Profits:" + str(increase_date) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits:" + str(decrease_date) + " ($" + str(greatest_decrease) + ")")

#to write to a text file in Analysis Folder. (Use \n for new line)
output_path = os.path.join("Analysis", "analysis.txt")
with open(output_path, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("--------------------------------------\n")
    text.write("Total Months: " + str(count) + "\n")
    text.write("Total: $" + str(total_profit) + "\n")
    text.write("Average Change: $" + str(int(average_change)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")\n")