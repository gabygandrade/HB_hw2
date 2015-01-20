"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

"""

salespeople = []
melons_sold = []

f = open("sales_report.csv")
for line in f:                    # for each line in the file 
    line = line.rstrip()          # strip all characters from the right side of each line and rebind to line
    entries = line.split(",")     # split each line by the commas and bind that to entries
    salesperson = entries[0]      # bind the first item in the entries list to the salesperson
    melons = int(entries[2])      # bind the third item in the entries list to melons and force it to become an integer

    if salesperson in salespeople:                      # if salesperson is in salespeople list
        position = salespeople.index(salesperson)       # bind position to the index number associated with where the salesperson is in the salespeople list 
        melons_sold[position] += melons                 # add the # of melons to the count of melons sold for each salesperson
    else:                                               # if the salesperson is not in the salespeople list
        salespeople.append(salesperson)                 # append the the name of the salesperson to the salespeople list
        melons_sold.append(melons)                      # append the number of melons to the melons_sold list


for i in range(len(salespeople)):                                   # for i in the range equal to the length of the salespeople list
    print "%s sold %d melons" % (salespeople[i], melons_sold[i])    # print this salesperson sold this # of melons
