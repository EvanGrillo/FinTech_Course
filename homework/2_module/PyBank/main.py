import csv

total_months = 0
total = 0
max_increase = {
    'date': '',
    'amount': 0
}
max_decrease = {
    'date': '',
    'amount': 0
}

# To do - rework without these variables
curr_val = None
price_changes = []

with open('Resources/budget_data.csv') as f:
    
    lines = f.readlines()
    
    # Skip header line in for loop
    for line in lines[1:]:
        
        # Use String split to parse row values with comma delimiter
        val1,val2 = line.split(',', 1)
        
        total_months += 1
        total += int(val2)
        
        # Use pointer to store current value to avoid extra steps
        if curr_val != None:
            
            diff = int(val2) - curr_val
            price_changes.append(diff)
            
            if diff > max_increase['amount']: 
                max_increase['date'] = str(val1)
                max_increase['amount'] = diff
            if diff < max_decrease['amount']: 
                max_decrease['date'] = str(val1)
                max_decrease['amount'] = diff

        curr_val = int(val2)

print(
    f'Total Months: {total_months}\n'
    f'Total: ${total}\n'
    f'Average Change: ${round(sum(price_changes) / len(price_changes), 2)}\n'
    f'Greatest Increase in Profits: {max_increase["date"]} ${max_increase["amount"]}\n'
    f'Greatest Decrease in Profits: {max_decrease["date"]} ${max_decrease["amount"]}\n'
)
