import os
import csv
#search for the file  to analyze
current_directory=os.getcwd()
csv_file_path=os.path.join(current_directory,'Resources','budget_data.csv')
#creates the file for the results and asigns its directory
outfolder_path= os.path.join(current_directory,'analysis')
out_file_path=os.path.join(outfolder_path, 'PyBankresults.txt')

with open (csv_file_path, newline='') as csvfile: #allows to use analyze the cvs file
    csvreader=csv.reader(csvfile) 

    next (csvreader) #skips the header

    #variables
    nettotal=0 #total net variable
    cRow=0 #monthsloop
    month1=0 #stores the value of one month
    month2=0 #stores the value of the next month
    pandl=0 #stores the change between months
    avg=0  #calculates the average of changes
    change=0 #sums all the changes of profit and loss
    results=[] #stores all the changes in a list
    date=[] #stores dates for changes
    output_content=[] #stores values for the txt file

    
    for row in  csvreader: #loops through cells
        cRow += 1 #counts the cells and adds 1 to its previous value (total months)
        nettotal += int (row[1]) #transforms each value in a integer number and accumulates it in the variable (total net)
        month2=int(row[1]) #stores value of next month (current month in the loop)  
        
        if month1!=0:
                   
            pandl=month2-month1 #calculates the change between months
            results.append(pandl) #adds each result to a list
            date.append(row[0]) #saves the date from the current row and the coumn that contains the string
            change=sum(results) #first step to calculate the average
            avg=change/len(results) #calculates the average, we use len to divide by the number of changes
        
        month1=month2 #sets current month as last month for the end of the loop
    
    #calculate greatest increase and finds value on the list
    increase=results.index(max(results))
    date_increase=date[increase]
    amm_increase=max(results)

    #calculates greatest decrease and finds value on the list
    decrease=results.index(min(results))
    date_decrease=date[decrease]
    amm_drecease=min(results)

#results get printed
print ("Financial Analysis")
print("-------------------------")
print (f"Total Months: {cRow}")
print (f"Total: {nettotal}")
print (f"Average change: {avg:.3f}")
print (f"Greatest increase in profits: {date_increase} ${amm_increase}")
print (f"Greatest decrease in profits: {date_decrease} ${amm_drecease}")

#we add all results to the list for the txt file
output_content.append("Financial Analysis")
output_content.append("-------------------------")
output_content.append(f"Total Months: {cRow}")
output_content.append(f"Total: ${nettotal}")
output_content.append(f"Average change: ${avg:.3f}")
output_content.append(f"Greatest increase in profits: {date_increase} ${amm_increase}")
output_content.append(f"Greatest decrease in profits: {date_decrease} ${amm_drecease}")

with open(out_file_path, 'w') as output_file: #we open the output file for the results, 'w' allows us to write on it
        for text in output_content: #we bring all we have in the outputcontent list
              output_file.write(f"{text}\n") #and finally print it all wirh '\n' to create spaces between the items of the list

