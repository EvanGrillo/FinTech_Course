import csv
from pathlib import Path

curr_dir = Path(__file__).resolve().parent
file_path = Path(f'{curr_dir}/Resources/budget_data.csv')

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

price_changes = []
data_list = []

with open(file_path) as f:
    
    reader = csv.DictReader(f)

    for row in reader:
        data_list.append(row)

    total_months = len(data_list)

    for i, dict in enumerate(data_list):

        total += int(dict["Profit/Losses"])

        #skip first item, no previous to compare
        if i == 0: continue
            
        prev = data_list[i-1]
        
        diff = int(dict["Profit/Losses"]) - int(prev["Profit/Losses"])
                
        price_changes.append(diff)

        if diff > max_increase['amount']: 
            max_increase['date'] = str(dict["Date"])
            max_increase['amount'] = diff
        if diff < max_decrease['amount']: 
            max_decrease['date'] = str(dict["Date"])
            max_decrease['amount'] = diff
    
print(
f"""
Total Months: {total_months}
Total: ${total}
Average Change: ${round(sum(price_changes) / len(price_changes), 2)}
Greatest Increase in Profits: {max_increase["date"]} ${max_increase["amount"]}
Greatest Decrease in Profits: {max_decrease["date"]} ${max_decrease["amount"]}
"""
)
