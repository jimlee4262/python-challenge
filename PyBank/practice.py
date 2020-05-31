import os
import csv

budget_file = os.path.join("Resources","budget_data.csv")
total_number_of_month = []
net_total = []
delta = []


with open(budget_file) as csvreader:
    csvreader = csv.reader(csvreader, delimiter = ",")

    #Skip header
    csv_header = next(csvreader)


    for row in csvreader:
        total_number_of_month.append(row[0])
        net_total.append(int(row[1]))

    for i in range(len(net_total)-1):
        delta.append((net_total[i + 1] - net_total[i]))

    #max
    max_value = max(delta)
    max_value_month = delta.index(max(delta))+1
    print(str(max_value))
    print(str(total_number_of_month[max_value_month]))

    #min
    min_value = min(delta)
    min_value_month = delta.index(min(delta))+1
    print(str(min_value))
    print(str(total_number_of_month[min_value_month]))

