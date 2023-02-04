import csv

#function to print output dictionary
def display(a_transactions):
    name_dict = {}
    for name, points, timestamp in a_transactions:
        if name in name_dict:
            name_dict[name] += int(points)
        else:
            name_dict[name] = int(points)
    print(name_dict)                                    #print final dictionary
    return name_dict                                    #return final dictionary


#recursive function to adjust points
def spend(i,points_out):
    difference = points_out - int(a_transactions[i][1])         #points out - points stored
    if difference > 0:                                          #points out > points stored
        a_transactions[i][1] = 0                                #subtract all possiblepoints from current transaction
        points_out = difference                                 # the difference is now new points_out
        i = i+1                                                 #go to the next value chronologically 
        spend(i,points_out)                                     #repeat until base condition is reached
    elif difference <= 0:                                       #Base: If difference is not positive,
        a_transactions[i][1] = abs(difference)                  #set points of current transaction as absolute value of difference
        

#function to sort transactions by timestamp
def sort_by_timestamp(transactions):
    return sorted(transactions, key=lambda x: x[2])


#main
transactions = []                                                #list to store contents of csv
i=0                                                              #set first index input for recursive function

# Read the CSV file and store transactions
with open("transactions_example.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)                                                #skip the header row
    for row in reader:
        transactions.append(row)

a_transactions = sort_by_timestamp(transactions)                # Sort the transactions by timestamp 

#fix initial file (remove and adjust all negative points)
for j in range(len(a_transactions)-1,-1,-1):                    #get indices in reverse order
    if int(a_transactions[j][1]) < 0:                           #check whether points are negative (from newest to oldest)
        points_out=abs(int(a_transactions[j][1])) 
        spend(i,points_out)                                     #call function to adjust points, start spending from oldest to newest
        a_transactions[j][1] = 0                                #set value of current transaction as 0

#print(a_transactions)
    
#spend amount entered (after fixing the original file)
points_out = int(input("Enter points"))                         #input from user; Enter number of point to be removed here
spend(i,points_out)                                             #call function to adjust points after handling negative points

display(a_transactions)                                         #call function to print final output dictionary
