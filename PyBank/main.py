import os
import csv

budget_csv = os.path.join(r"PyBank/Resources/budget_data.csv")

with open(budget_csv, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    total_months = 0
    net_total_profit_loss = 0
    changes = []
    dates = []
    prior_profit_loss = None

    for row in csv_reader:
        total_months += 1
        net_total_profit_loss += int(row['Profit/Losses'])
        profit_loss = int(row['Profit/Losses'])
        dates.append(row['Date'])

        if prior_profit_loss is not None:
            profit_changes = profit_loss - prior_profit_loss
            changes.append(profit_changes)

        prior_profit_loss = profit_loss

# Calculate the average of the changes in profit/loss over the entire period
average_profit_change = sum(changes) / len(changes)

# Determine the greatest profit increase and decrease with the respective dates (+1 to factor in the start at 0)
greatest_profit_increase = max(changes)
greatest_profit_increase_date = dates[changes.index(greatest_profit_increase)+1]

greatest_profit_decrease = min(changes)
greatest_profit_decrease_date = dates[changes.index(greatest_profit_decrease)+1]

# Final Analysis in Terminal
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_profit_loss}")
print(f"Average Change: ${round(average_profit_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_profit_increase_date} (${greatest_profit_increase})")
print(f"Greatest Decrease in Profits: {greatest_profit_decrease_date} (${greatest_profit_decrease})")

#export a text file with the results

output_path = os.path.join(r"PyBank/Analysis/budget_analysis.txt")

with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total_profit_loss}\n")
    output_file.write(f"Average Change: ${round(average_profit_change, 2)}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_profit_increase_date} (${greatest_profit_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_profit_decrease_date} (${greatest_profit_decrease})\n")

