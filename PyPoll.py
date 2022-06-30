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


#add our dependencies.
import csv
import os

# assign variable to load a file to a path
file_to_load = os.path.join('/Users/caed/Desktop/Data_Repository/Election_Analysis/Resources/election_results.csv')
# Assign a variable to save the file to path
file_to_save = os.path.join("/Users/caed/Desktop/Data_Repository/Election_Analysis/analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:
   
    # To do: read and analyze the data.
    #read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    print(headers)
    #print each row in the CSV file
    for row in file_reader:
        print(row)
        

# 1. The total number of votes cast.
# 2. A complete list of votes each candidate won.
# 3. A complete list of candidates who recieved votes.
# 4. The total number of votes each candidate won. 
# 5. The winner of the election based on popular vote. 