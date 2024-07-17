import os
import csv

# Set the working directory
os.chdir(r'/Users/oumadiak99/Desktop/Homework Challenge/python-challenge/PyPoll/Resources')

# Read the election data file
file_path = 'election_data.csv'  # Replace with your actual file name if different

total_votes = 0
candidate_votes = {}

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header
    
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Display the results in the desired format
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open("/Users/oumadiak99/Desktop/Homework Challenge/python-challenge/PyPoll/analysis/PyPoll.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        file.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
