#Create a python script that analyzes the votes and calculates following values:
#the total number of votes
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#the total number of votes each candidate won
#the winner of the election bases on popular votes


#Dependencies
import os
import csv
from collections import Counter

#variables
candidates = []
votes = {}
total_votes = 0

#set path for file
cvspath = os.path.join ("Resources","election_data.csv")

#open the csv
with open(cvspath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        candidate_name = row[2] 
        total_votes +=1
        
        if candidate_name not in candidates: 
            candidates.append (candidate_name)
            votes[candidate_name] = 0
        votes[candidate_name] += 1

# print (total_votes)
# print (votes)

percentages = {key: val / total_votes*100 for key, val in votes.items()}

# print (percentages)

winner = max(votes, key=votes.get)
# print(winner)


print("\n") 
print("Election Results")
print("-------------------------------")
print(f'Total Votes: {total_votes}') 
print("-------------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes[candidate]})")
print("-------------------------------")
print(f'Winner: {winner}')
print("-------------------------------")
print("\n") 


#print analysis to the terminal and export a text file with the results
export = os.path.join("Analysis","PyPoll_text.txt")
with open(export, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------------\n")
    textfile.write(f'Total Votes: {total_votes}\n')
    for candidate in candidates:
        textfile.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes[candidate]})\n")
    textfile.write("-------------------------------\n")
    textfile.write(f'Winner: {winner}\n')
    textfile.write("-------------------------------\n")












