LAST_DIGIT = 6 
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

for day in range(1, 8):
    amount = int(input(f"Day {day}: "))
    expenses.append(amount)

total = 0
highest_val = expenses[0]
highest_day = 1
above_limit = 0

for i in range(len(expenses)):
    val = expenses[i]
    total += val
    
    if val > highest_val:
        highest_val = val
        highest_day = i + 1
        
    if val > daily_limit:
        above_limit += 1

average = total / len(expenses)

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest_val})")
print(f"Days above limit: {above_limit}")