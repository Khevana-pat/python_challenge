import csv
import os
#path for resource file and output file 
csvpath = r"C:\Users\rushi\Downloads\Python_assignment\python_challenge\PyBank\resources\budget_data.csv"
analysis = r"C:\Users\rushi\Downloads\Python_assignment\python_challenge\PyBank\analysis\analysis.text"
# open csv in readmode
with open(csvpath, 'r') as csvfile:

    #Read csv
    reader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(reader)

    #  variables for counting 
    dates = []
    money = []
    change =[]
    change_alt = []
    previous = 0

    #Revenue list will be a list of int
    for row in reader:
        dates.append(row[0])
        money.append(row[1])
        
        diff = int(row[1]) - int(previous)
        previous = row[1]
        change.append(diff)

#Loop through revenue indices and compare
zipped = zip(dates, change)
zipped_lst = list(zipped)
change.remove(change[0])
zipped_lst.remove(zipped_lst[0])

# total months
total_months = len(dates)
total = sum(map(int, money))
#Calculate average_change
average_change = sum(change) / len(change)
#Create greatest increase, decrease variables and the match for the months
increase = max(change)
decrease = min(change)
month_dec = 0
month_inc = 0

##To find greatest inc and dec
for row in zipped_lst:
    if row[1] == increase:
        month_inc = row[0]
    if row[1] == decrease:
        month_dec = row[0]

# Opens the analysis.text in write mode and prints the summary
with open(analysis, 'w') as text_file:
    print(f'Financial Analysis', file=text_file)
    print(f'___________________________', file=text_file)
    print(f'Total Months: {total_months}', file=text_file)
    print(f'Total: ${total}', file=text_file)
    print(f'Average Change: ${average_change:.2f}', file=text_file)
    print(f'Greatest Increase in Profits: {month_inc} ({increase})', file=text_file)
    print(f'Greatest Decrease in Profits: {month_dec} ({decrease})', file=text_file)

#opens the analysis.text in r mode and prints to terminal
analysis = os.path.join(analysis)
with open(analysis, 'r') as readfile:
    print(readfile.read())