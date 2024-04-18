import os
import csv
#search for the file  to analyze
current_directory=os.getcwd()
csv_file_path=os.path.join(current_directory,'Resources','election_data.csv')
#creates the file for the results and asigns its directory
outfolder_path= os.path.join(current_directory,'analysis')
out_file_path=os.path.join(outfolder_path, 'PyPollresults.txt')

with open (csv_file_path, newline='') as csvfile: #allows to use analyze the cvs file
    csvreader=csv.reader(csvfile)

    next (csvreader) #skips the header
    
    votes= {} #directory to store votes
    for row in csvreader: #loops through rows
        candidate=row[2] #assigns the column for each candidate
        if candidate in votes:
            votes[candidate]+=1 #starts storing the votes
        else:
            votes[candidate]=1 #if not keeps it the same
    
    totalvotes=sum(votes.values()) #calculates the total ammount of votes

    output_content =[] #we create a list to be able to send all the prints to our text  file

    #stores each print needed for the txt file
    output_content.append("Election results")
    output_content.append("------------------------")
    output_content.append(f"Total Votes: {totalvotes}")
    output_content.append("------------------------")

    #We also print in the console the value for the total votes
    print ("Election results")
    print ("------------------------")
    print (f"Total Votes: {totalvotes}")
    print ("------------------------")

    for candidate, count_count in votes.items(): #to calculate the percentage we count the votes (with count_count) for each candidate in the list votes
        per = (count_count/totalvotes)*100 #formula for the percentage
        perprint= f"{candidate}:{per:.3f}% ({count_count})"  #we create a variable for the result and give it percentage format with 3 decimals
        print(perprint) #we print the results
        output_content.append(perprint) #stores values of the result for the txt file

    win=max(votes, key=votes.get) #gets the maximum value in the votes  list
    
    print ("------------------------")
    print (f"Winner: {win}")
    print ("------------------------")

    output_content.append("------------------------")
    output_content.append(f"Winner: {win}") #saves the winner value for the txt file
    output_content.append("------------------------")

    with open(out_file_path, 'w') as output_file: #we open the output file for the results, 'w' allows us to write on it
         for text in output_content: #we bring all we have in the outputcontent list
              output_file.write(f"{text}\n")  #and finally print it all wirh '\n' to create spaces between the items of the list
