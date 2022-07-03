# The data we need to retrieve.
# import datetime class from the datetime module
import datetime as dt

# Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()

# Print the present time
print("the time right now is ", now)

# Add dependencies
# Import CSV
import csv

# Import os
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join('/Users/caed/Desktop/Data_Repository/Election_Analysis/Resources/election_results.csv')


#open election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis
    print(election_data)

# Assign a variable ti load a file from a path
file_to_save = os.path.join("/Users/caed/Desktop/Data_Repository/Election_Analysis/analysis", "election_analysis.txt")

# Using with statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #write some data to the file
    txt_file.write("Counties in Election\n---------------------\nArapahoe\nDenver\nJefferson")


# assign variable to load a file to a path
file_to_load = os.path.join('/Users/caed/Desktop/Data_Repository/Election_Analysis/Resources/election_results.csv')
# Assign a variable to save the file to path
file_to_save = os.path.join("/Users/caed/Desktop/Data_Repository/Election_Analysis/analysis", "election_analysis.txt")

# initialize a total_vote counter
total_votes = 0

#  Candidate options
candidate_options = []

# Winning candidate and winning count tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0

# Declare empty candidate votes dictionary
candidate_votes = {}
#open the election results and read the file
with open(file_to_load) as election_data:
   
    # To do: read and analyze the data.
    #read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    

    # 1. The total number of votes cast.
    for row in file_reader:

         # 2. Add to the total vote count
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        # 3. A complete list of candidates who recieved votes.
        # If the candidate does not ,atch an existing candidate.
        if candidate_name not in candidate_options:

            # Add it to the list of candidates
            candidate_options.append(candidate_name)    

            # 4. The total number of votes each candidate won. 
            #Begin tracking corresponding candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to the corresponding candidate's count
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
            # print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
        
    txt_file.write(election_results)
   

# Print candidate list.
#print(candidate_votes)

# Detirmine the percentage of votes for each candidate by looping through the counts
# 1. iterate through the candidate list
    for candidate_name in candidate_votes:

    # 2. Retrieve the vote count of a candidate.
        votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out eaach candidate's name, vote count, and percentage of 
    # votes to terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Detirmine winning vote count and candidate
    # 1. Detirmine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

        # 2. If true then set winning_count = votes and winning percentage.
        # Vote percentage
            winning_count = votes
            winning_percentage = vote_percentage

        # 3. set winning_candidate equal to candidate_name
            winning_candidate = candidate_name

        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
        # Define candidate_results
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #print each candidate, their voter count and percentage to the terminal
        print(candidate_results) 
        # save candidate results to the txt file
        txt_file.write(candidate_results)
    # Save the winning candidates name to the text file 
    txt_file.write(winning_candidate_summary)