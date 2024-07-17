import os
import csv

# Set the working directory
os.chdir(r'/Users/oumadiak99/Desktop/Homework Challenge/python-challenge/PyBank/Resources')

#budget_data = os.path.join("/Users/oumadiak99/Desktop/Resources", "budget_data.csv")



# Read the budget data file
file_path = 'budget_data.csv'  # Replace with your actual file name if different

dates = []
profits_losses = []

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# Calculate the total number of months included in the dataset
total_months = len(dates)

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = sum(profits_losses)

# Calculate the changes in "Profit/Losses" over the entire period
changes = [profits_losses[i] - profits_losses[i - 1] for i in range(1, len(profits_losses))]

# Calculate the average of those changes
average_change = sum(changes) / len(changes)

# Find the greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase) + 1]

# Find the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]

# Display the results in the desired format
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")