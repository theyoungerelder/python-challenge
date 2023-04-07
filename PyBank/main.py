# read data into python
with open('budget_data.csv', 'r') as data:

    # set starting point for variables
    months = 0
    net_total = 0
    greatest_increase = 0
    greatest_decrease = 0
    changes = []
    dates = []

    # there is a header in the data set. this skips it. i think...
    next(data)

    # loop through the rows
    for rows in data:
        # split the line into a list of values
        row = rows.split(',')

        # add one to the count of months
        months = months + 1

        # create a net total and add the profit/losses. 
        net_total = net_total + int(row[1])

        # add to dates lis
        dates.append(row[0])

        # month changes 
        if len(changes) > 0:
            change = int(row[1]) - int(changes[-1])
            changes.append(change)
        else:
            change = 0
            changes.append(change)

        # check increase adn decrease
        if change > greatest_increase:
            greatest_increase = change
            increase_date = row[0]
        elif change < greatest_decrease:
            greatest_decrease = change
            decrease_date = row[0]

# average change
average_change = sum(changes) / len(changes)

# print my results
print("Total Months: ", months)
print("Net Total: $", net_total)
print("Average Change: $", round(average_change, 2))
print("Greatest Increase in Profits: ", increase_date, "($", greatest_increase, ")")
print("Greatest Decrease in Profits: ", decrease_date, "($", greatest_decrease, ")")

# make file to put analysis into
with open('results.txt', 'w') as file:

# Write data to file
    file.write("Total Months: " + str(months) + "\n")
    file.write("Net Total: $" + str(net_total) + "\n")
    file.write("Average Change: $" + str(round(average_change, 2)) + "\n")
    file.write("Greatest Increase in Profits: " + increase_date + " ($" + str(greatest_increase) + ")\n")
    file.write("Greatest Decrease in Profits: " + decrease_date + " ($" + str(greatest_decrease) + ")\n")




