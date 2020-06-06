import os
import csv

voter_ID = []
county = []
candidate = []
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0
otooley_name = "0'Tooley"

#locating election_data.csv file
election_data = os.path.join("Resources","election_data.csv")

#Opening election_data.csv file
with open(election_data) as csvreader:
    csvreader = csv.reader(csvreader, delimiter = ",")

    #Skip header
    csv_header = next(csvreader)

    #Puts eacch column into an array
    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    #counts the # of votes for each candidacy
    for i in candidate:
        if i == "Khan":
            khan_vote = khan_vote + 1
        elif i == "Correy":
            correy_vote = correy_vote + 1
        elif i == "Li":
            li_vote = li_vote + 1
        else:
            otooley_vote = otooley_vote + 1

    # calculates voters percentage in decimlal
    total_vote = khan_vote + correy_vote + li_vote + otooley_vote
    khan_decimal = round(khan_vote / total_vote, 3)*100
    correy_decimal = round(correy_vote / total_vote, 3)*100
    li_decimal = round(li_vote / total_vote, 3)*100
    otooley_decimal = round(otooley_vote / total_vote, 3)*100

    #converts to percent
    khan_percent = format(khan_decimal, ".3f")
    correy_percent = format(correy_decimal, ".3f")
    li_percent = format(li_decimal, ".3f")
    otooley_percent = format(otooley_decimal, ".3f")

    #prints results
    print("'''text")
    print('-------------------------')
    print("total votes: " + str(len(voter_ID)))
    print('-------------------------')
    print(f'Khan: {khan_percent}% ({khan_vote})')
    print(f'Correy: {correy_percent}% ({correy_vote})')
    print(f'Li: {li_percent}% ({li_vote})')
    print(f'{otooley_name}: {otooley_percent}% ({otooley_vote})')
    print('-------------------------')
    print(f'Winner: Khan')
    print('-------------------------')
    print("'''")

#saves it out with the written text
# Dependencies

output_path = os.path.join("analysis", "election_analysis.txt")
with open(output_path, 'w') as csvfile:


    # Write the first row (column headers)
    csvfile.write("'''text")
    csvfile.write("\n")
    csvfile.write('-------------------------')
    csvfile.write("\n")
    csvfile.write("total votes: " + str(len(voter_ID)))
    csvfile.write("\n")
    csvfile.write('-------------------------')   
    csvfile.write("\n")
    csvfile.write(f'Khan: {khan_percent}% ({khan_vote})')
    csvfile.write("\n")    
    csvfile.write(f'Correy: {correy_percent}% ({correy_vote})')
    csvfile.write("\n")    
    csvfile.write(f'Li: {li_percent}% ({li_vote})')
    csvfile.write("\n")    
    csvfile.write(f'{otooley_name}: {otooley_percent}% ({otooley_vote})')
    csvfile.write("\n")    
    csvfile.write('-------------------------')
    csvfile.write("\n")
    csvfile.write(f'Winner: Khan')
    csvfile.write("\n")
    csvfile.write('-------------------------')
    csvfile.write("\n")
    csvfile.write("'''")
