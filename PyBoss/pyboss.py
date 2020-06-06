# importing modules
import os
import csv

employee_id = []
employee_name = []
employee_first = []
employee_last = []
employee_dob = []
employee_dob_month = []
employee_dob_day = []
employee_dob_year = []
employee_ssn = []
employee_new_ssn = []
employee_state = []
employee_abbreviated_state = []
employee_dob_newdate = []

#state abbreviation 
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# importing the file
employee_data = os.path.join('employee_data.csv')

#Opening election_data.csv file
with open(employee_data) as csvreader:
    csvreader = csv.reader(csvreader, delimiter = ",")

    #Skip header
    csv_header = next(csvreader)

    #Puts eacch column into an array
    for row in csvreader:
        employee_id.append(row[0])
        employee_name.append(row[1])
        employee_dob.append(row[2])
        employee_ssn.append(row[3])
        employee_state.append(row[4])
    
    #split name into first and last
    for i in employee_name:
        first, last = i.split(' ')
        employee_first.append(first)
        employee_last.append(last)

    #split MM/DD/YYYY into 3 different arrays
    for j in employee_dob:
        year, month, day = j.split("-")
        employee_dob_year.append(year)
        employee_dob_month.append(month)
        employee_dob_day.append(day)
        employee_dob_newdate.append(month + "/" + day + "/" + year)

    #covering digits for social security with *
    for k in employee_ssn:
        new_ssn = '***-**-' + str(k[-4:])
        employee_new_ssn.append(new_ssn)

    #translates states to abbreviated states
    for state in employee_state:
        employee_abbreviated_state.append(us_state_abbrev[state])

    #zip everything together
    combine_everything = zip(employee_id, employee_first, employee_last, employee_dob_newdate, employee_new_ssn, employee_abbreviated_state)

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    writer.writerows(combine_everything)

