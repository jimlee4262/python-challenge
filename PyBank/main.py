# importing modules
import os
import csv

# importing the file
budget_file = os.path.join('Resources','budget_data.csv')
print(budget_file)

total_months = []
net_total = []
net_total_change = []

with open(budget_file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skips header
    csv_header = next(csvreader)

    for row in csvreader:

        #adding months
        total_months.append(row[0])

        #adding net_total
        net_total.append(int(row[1]))

    # Calculates the delta for each net total 
    for i in range(len(net_total)-1):
        
        # Finds the difference between profit and loss
        net_total_change.append(net_total[i+1]-net_total[i])

    #find max
    max_increase = max(net_total_change)
    max_increase_month = net_total_change.index(max(net_total_change)) + 1
    
    #find min
    max_decrease = min(net_total_change)
    max_decrease_month = net_total_change.index(min(net_total_change)) + 1   

    print('Financial Analysis')
    print('----------------------------')
    print('Total Months: ' + str(len(total_months)))
    print('Total: $' + str(sum(net_total)))
    print("Average Change: $" + str(round(sum(net_total_change)/len(net_total_change),2)))
    print(f'Greatest Increase in Profits: {total_months[max_increase_month]} (${max_increase})')
    print(f'Greatest Decrease in Profits: {total_months[max_decrease_month]} (${max_decrease})')
    print('---')

#saves it out with the written text
# Dependencies

output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, 'w') as csvfile:


    # Write the first row (column headers)
    csvfile.write('Financial Analysis')
    csvfile.write("\n")
    csvfile.write('----------------------------')
    csvfile.write("\n")
    csvfile.write('Total Months: ' + str(len(total_months)))
    csvfile.write("\n")    
    csvfile.write('Total: $' + str(sum(net_total)))
    csvfile.write("\n")    
    csvfile.write("Average Change: $" + str(round(sum(net_total_change)/len(net_total_change),2)))
    csvfile.write("\n")    
    csvfile.write(f'Greatest Increase in Profits: {total_months[max_increase_month]} (${max_increase})')
    csvfile.write("\n")    
    csvfile.write(f'Greatest Decrease in Profits: {total_months[max_decrease_month]} (${max_decrease})')
    csvfile.write("\n")    
    csvfile.write('---')    
