import os
import csv

# Define the file path
election_data = r"PyPoll/Resources/election_data.csv"

# Initialize variables
total_votes = 0
candidate_votes = {}
candidates_names = []


# Read the CSV file
with open(election_data, 'r') as file:
    csv_reader = csv.reader(file)
    csv_header=next(csv_reader)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Count total votes
        total_votes += 1

        # Extract candidate name from the row
        candidate = row[2]

        
        if candidate not in candidates_names:
            candidates_names.append(candidate)
        
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

#Set up to calculate the winner
max_percentage_votes_per_candidate = 0
winner = ""

# Determine percentage of votes per candidate
for candidate in candidates_names:
    percentage_votes_per_candidate = (candidate_votes[candidate] / total_votes) * 100

    if percentage_votes_per_candidate > max_percentage_votes_per_candidate:
        max_percentage_votes_per_candidate = percentage_votes_per_candidate
        winner = candidate

# Print Election Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates_names:
    percentage_votes_per_candidate = (candidate_votes[candidate] / total_votes) * 100
    print(f"{candidate}: {percentage_votes_per_candidate:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
    
#Export a text file with the results

output_path = os.path.join(r"PyPoll/Analysis/results.txt")

with open(output_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate in candidates_names:
        percentage_votes_per_candidate = (candidate_votes[candidate] / total_votes) * 100
        output_file.write(f"{candidate}: {percentage_votes_per_candidate:.3f}% ({candidate_votes[candidate]})\n")
    output_file.write(f"-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write(f"-------------------------\n")