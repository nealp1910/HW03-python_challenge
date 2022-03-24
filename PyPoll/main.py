# 1.    The total number of votes cast
# 2.    A complete list of candidates who received votes
# 3.    The percentage of votes each candidate won
# 4.    The total number of votes each candidate won
# 5.    The winner of the election based on popular vote.

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

# import os and csv module
import os
import csv

#List and variables
candidates = []
total_votes = []
percent = []
count = 0

#csv path file
csvpath = os.path.join('Resources', 'election_data.csv')

# open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f'CSV Header: {csv_header}') - checksome to see if headers are being printed in terminal 

    for row in csvreader:
        #print(row) - checksome to see if data is being printed in terminal
        count += 1

        # check if candidate is in list or not
        if row[2] not in candidates:
            candidates.append(row[2])
            total_votes.append(1)
        
        else:
            candidate_index = candidates.index(row[2])
            total_votes[candidate_index] += 1

# calculate percent vote
    for votes in total_votes:
        percentage = (votes / count) * 100
        percentage = float(percentage)
        percentage = round(percentage, 3)
        percent.append(percentage)

    # to find the winning candidate
    winner = max(total_votes)
    candidate_index = total_votes.index(winner)
    candidate_winner = candidates[candidate_index]

#print statements
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(count))
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent[i])} ({str(total_votes[i])})")
print("-------------------------")
print("Winner: " + str(candidate_winner))
print("-------------------------")

# to write to a text file in Analysis folder. use \n for new line
output_path = os.path.join("Analysis", "PyPoll_analysis.txt")
with open(output_path, 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Votes: " + str(count) + "\n")
    for i in range(len(candidates)):
        text.write(f"{candidates[i]}: {str(percent[i])} ({str(total_votes[i])})" + "\n")
    text.write("-------------------------\n")
    text.write("Winner: " + str(candidate_winner) + "\n")
    text.write("-------------------------")
