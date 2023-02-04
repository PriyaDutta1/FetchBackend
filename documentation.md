# Structure
1. The program reads a csv file named transactions and stores it as a list (with each transaction as an element)
2. sort_by_timestamp(list) sorts the transactions in ascending order of timestamp (oldest at index 0)
3. then the file read is searched for negative payer points (see Assumptions). The file is searched from newest to oldest transaction. If a transaction with negative points is found, its value is spent (using spend(i,points)) starting from the oldest transaction (index 0) to the transaction immediately before the transaction with negative points.
4. Now, the program will ask the user for an input in the form of an integer points (to spend)
5. Depending on the value of the input in step 5 and the conditions specified in the googe doc, points are spent from the adjusted list (without negative points)
6. display(list) uses a dictionary to read, order, and display payers as keys and total points(of a payer) as values of the dictionary
7. The only output of the program should be a dictionary of key:value pairs (line 11 of program.py)

# Assumptions
1. I didn't quite understand how negative point values already in the csv file are supposed to be handled. Going by the example provided, I assumed that negative points were adjusted by removing the absolute value of the negative point from transactions older than the transaction with a negative point. So, the program removes all the negative points from the list first and then works on removing the points in putted
2. The program isn't tested for all edge cases. It is also not fully optimized. Since the google doc said that the question was designed to take a few hours to complete, I figured in-depth testing and a 100% optimized code is not expected. (Current Runtime should be O(n), I haven't tried to reduce it any further)
