### Financial Analysis ###

#Input modules for analysis
import os
import csv

#Set path for file
csvpath = os.path.join("python-challenge","Starter_Code","PyBank","Resources","budget_data.csv")
#print(csvpath)

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Has headers so use below to skip header
    next(csvfile)
    #Read through each row of data after the header
    row_count = sum(1 for row in csv_reader) 
    print(f'Total Months: {row_count}')

#Sum the profit/losses column
#Using following link to refresh on for loop counters accessing the index value:https://stackoverflow.com/questions/522563/how-to-access-the-index-value-in-a-for-loop
with open(csvpath) as csvfile:
     #Skipping header row
     next(csvfile)
     #Initializing counter 
     total = 0
     for row in csv.reader(csvfile):
         total += int(row[1]) #Adding the values in the second column
print(f'Total: ${total}')

#Calculate Average Change
#initialize empty list to store changes
changes = []

#Using similar for loop logic as my script in the vba-challenge but in python 
with open(csvpath) as csvfile:
     csv_reader = list(csv.reader(csvfile, delimiter=","))
     #Skipping header and first row by starting range at the second position
     for i in range(2, len(csv_reader)):
        # Calculate change from the profit/loss column in the current row from previous row
          current = csv_reader[i][1] #current for loop row amount
          previous = csv_reader[i-1][1] # previous for loop row amount
          change = float(current) - float(previous)
          changes.append(change) # add the change amount to the changes list to index later

#Find index for the greatest increase and greatest decrease to print dates.
#Use this link for index function refresher https://www.geeksforgeeks.org/python-list-index/
max_index = changes.index(max(changes))+2 #Adding plus two because we started at the second position in changes list
min_index = changes.index(min(changes))+2   

average = round(sum(changes) / len(changes),2)
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {csv_reader[max_index][0]} (${max(changes)})')
print(f'Greatest Decrease in Profits: {csv_reader[min_index][0]} (${min(changes)})')

output_path = os.path.join("python-challenge","Starter_Code","PyBank","analysis", "output.txt")

with open(output_path, "w") as out_file:
     print(f'Total Months: {row_count}')
     print(f'Total: ${total}')
     print(f'Average Change: ${average}')
     print(f'Greatest Increase in Profits: {csv_reader[max_index][0]} (${max(changes)})')
     print(f'Greatest Decrease in Profits: {csv_reader[min_index][0]} (${min(changes)})')

