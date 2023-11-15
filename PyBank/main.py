# Create Python script that analyzes the records
# connect to dataset budget_data.csv
# Calculate total number of months included in the dataset
# Calculate the net total amount "profit/losses" over the entire period
# Calculate the changes in "profit/losses over the entire period,
# ..and then the average of those changes"
# Calculate the greatest increase in profits (data and amount) over the entire period
# Calculate the greatest decrease in profits (date and amount) over the entire period

#Import dependancies
import os
import csv

#Define PyBank's variables
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous = 0
current_month_profit_loss = 0
profit_loss_change = 0

# read the csv file
filepath = os.path.join("Resources","budget_data.csv")

with open(filepath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        #print(row)
        months.append(row[0])
        net_profit_loss += int(row[1])
        
        if previous != 0:
            profit_loss_changes.append(int(row[1]) - previous)

        previous = int(row[1])
        



    # after the for loop completes
    #print(len(months))

    for i in range(len(profit_loss_changes)-1):
        if i == 0:
            gpinc = i
            gpdec = i
        else:
            if int(profit_loss_changes[i]) > int(profit_loss_changes[gpinc]):
                gpinc = i
            if int(profit_loss_changes[i]) < int(profit_loss_changes[gpdec]):
                gpdec = i


#after the csv file is read, display the results
#
print("\n") 
print("Financial Analysis")
print("-------------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: ${(net_profit_loss)}')
print(f'Average Change: ${(sum(profit_loss_changes) / len(profit_loss_changes)):.2f}') 
print(f'Greatest Increase in Profits: {months[gpinc+1]} (${profit_loss_changes[gpinc]})  ')
print(f'Greatest Decrease in Profits: {months[gpdec+1]} (${profit_loss_changes[gpdec]})  ')
print("\n") 

export = os.path.join("Analysis","PyPoll_text.txt")
with open(export, "w") as textfile:

    textfile.write("Financial Analysis \n")
    textfile.write("-------------------------------\n")
    textfile.write(f'Total Months: {len(months)}\n')
    textfile.write(f'Total: ${(net_profit_loss)}\n')
    textfile.write(f'Average Change: ${(sum(profit_loss_changes) / len(profit_loss_changes)):.2f}\n') 
    textfile.write(f'Greatest Increase in Profits: {months[gpinc+1]} (${profit_loss_changes[gpinc]})\n')
    textfile.write(f'Greatest Decrease in Profits: {months[gpdec+1]} (${profit_loss_changes[gpdec]})\n')







