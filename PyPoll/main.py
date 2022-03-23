# import os and csv modules
import os
import csv

#csv path file
csvpath = os.path.join('Resources', 'election_data.csv')

#list to store data
votes = []

# to open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) 
    # print(f'CSV Header: {csv_header}')

    for row in csvreader:
        # print(row)



print("Election Results")
print("---------------------------")
print("Total Votes: ")
print("")
print("")
print("")
print("---------------------------")
print("Winner: ")
print("---------------------------")